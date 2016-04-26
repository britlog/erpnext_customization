# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
import frappe.defaults

def update_website_context(context):
	context["footer_company_name"] = frappe.db.get_value("Website Settings", "Website Settings", "footer_company_name")
	context["facebook_link"] = frappe.db.get_value("Website Settings", "Website Settings", "facebook_link")
