import frappe
from frappe.utils import nowdate
from erpnext.accounts.doctype.payment_request.payment_request import make_payment_request
import stripe


def make_sales_order(customer, item_code, name, email):
	doc = frappe.get_doc({
		"doctype": "Sales Order",
		"customer": customer,
		"items": [{
			'doctype': 'Sales Order Item',
			'item_code': item_code,
			'qty': 1
		}],
		"po_no": name,
		"contact_email": email,
		"company": frappe.db.get_single_value("Global Defaults", "default_company"),
		"delivery_date": nowdate()
	})
	doc.flags.ignore_permissions = True
	doc.run_method("set_missing_values")
	doc.insert()
	doc.submit()

	return doc


@frappe.whitelist(allow_guest=True)
def create_payment_request(name, email):
	# create sales order
	so_doc = make_sales_order("Buzug", "00BUZUG10", name, email)

	# Create payment request
	pr_doc = make_payment_request(dt="Sales Order", dn=so_doc.name, recipient_id=so_doc.contact_email, submit_doc=True,
							  mute_email=True, return_doc=True)
	frappe.db.commit()

	# Create a PaymentIntent with the amount, currency, and a payment method type.
	#
	# See the documentation [0] for the full list of supported parameters.
	#
	# [0] https://stripe.com/docs/api/payment_intents/create
	stripe.api_key = "sk_test_dk9SxaebXF6A37P7zk4GGZwl"
	try:
		intent = stripe.PaymentIntent.create(
			amount=int(so_doc.grand_total * 100),
			currency=so_doc.currency,
			automatic_payment_methods={
				'enabled': True,
			},
			metadata={
				'payment_request': pr_doc.name,
			}
		)

		# Send PaymentIntent details to the front end.
		return {'clientSecret': intent.client_secret}
	except stripe.error.StripeError as e:
		return {'error': {'message': str(e)}}, 400
	except Exception as e:
		return {'error': {'message': str(e)}}, 400


@frappe.whitelist(allow_guest=True)
def payment_status():
	# You can use webhooks to receive information about asynchronous payment events.
	# For more about our webhook events check out https://stripe.com/docs/webhooks.
	webhook_secret = "whsec_n7aEa0vPufIwtvaJE3kFaGD6mdIcVsb6"

	if webhook_secret:
		# Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
		signature = frappe.get_request_header('stripe-signature')
		try:
			event = stripe.Webhook.construct_event(
				payload=frappe.request.data, sig_header=signature, secret=webhook_secret)
			data = event['data']
		except Exception as e:
			frappe.log_error(e)
			return e
		# Get the type of webhook event sent - used to check the status of PaymentIntents.
		event_type = event['type']
	else:
		data = frappe.form_dict['data']
		event_type = frappe.form_dict['type']
	data_object = data['object']

	if event_type == 'payment_intent.succeeded':
		# To cancel the payment you will need to issue a Refund (https://stripe.com/docs/api/refunds)
		# Create payment entry
		frappe.get_doc("Payment Request", data_object["metadata"]["payment_request"]).run_method("set_as_paid")
	elif event_type == 'payment_intent.payment_failed':
		frappe.log_error('Payment failed')
	return {'status': 'success'}

