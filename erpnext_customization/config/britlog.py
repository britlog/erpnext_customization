from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": "Mailjet",
			"icon": "fa fa-envelope",
			"items": [
				{
					"type": "doctype",
					"name": "Email Tracking",
					"label": _("Email Tracking"),
					"description": _("Track emails to increase deliverability.")
				}
			]
		}
	]

