# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "erpnext_customization"
app_title = "Erpnext Customization"
app_publisher = "britlog"
app_description = "App to maintain custom changes"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_version = "0.0.1"
app_email = "info@britlog.com"
app_license = "MIT"
source_link = "https://github.com/britlog/erpnext_customization"

fixtures = ["Custom Field",
"Property Setter",
"Custom Script",
"Print Format"]


# website
update_website_context = "erpnext_customization.website.utils.update_website_context"

#website_context = {
#	"footer_company_name": 	"settings.footer_company_name"
#}




# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_customization/css/erpnext_customization.css"
# app_include_js = "/assets/erpnext_customization/js/erpnext_customization.js"

# includes to get back to summernote editor
# quill replaces summernote in v11 but less flexible
app_include_js = [
	"assets/js/summernote.min.js",
	"assets/js/comment_desk.min.js",
	"assets/js/editor.min.js",
	"assets/js/timeline.min.js"
]

app_include_css = [
	"assets/css/summernote.min.css"
]

# include js, css files in header of web template
web_include_css = "/assets/erpnext_customization/css/website.css"
# web_include_js = "/assets/erpnext_customization/js/shopping_cart.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_customization.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_customization.install.before_install"
# after_install = "erpnext_customization.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_customization.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_customization.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_customization.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_customization.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_customization.event.get_events"
# }
