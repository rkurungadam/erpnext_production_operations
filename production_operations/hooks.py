app_name = "production_operations"
app_title = "Production Operations"
app_publisher = "earthians"
app_description = "Creates Operations in Production Order based on BOM operations"
app_icon = "icon-tasks"
app_color = "#7f8c8d"
app_email = "ranjith@earthianslive.com"
app_url = "https://frappe.io/apps"
app_version = "0.0.1"

notification_config = "production_operations.production_operations.notifications.get_notification_config"

doc_events = {
	"Production Order": {
		"on_submit": "production_operations.production_operations.doctype.production_operations.production_operations.create_operations",
		"on_cancel": "production_operations.production_operations.doctype.production_operations.production_operations.cancel_operations",
	}
}

override_whitelisted_methods = {
	"erpnext.manufacturing.doctype.production_order.production_order.make_stock_entry": "production_operations.production_operations.doctype.production_operations.production_operations.validate_operations",
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/production_operations/css/production_operations.css"
# app_include_js = "/assets/production_operations/js/production_operations.js"

# include js, css files in header of web template
# web_include_css = "/assets/production_operations/css/production_operations.css"
# web_include_js = "/assets/production_operations/js/production_operations.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "production_operations.install.before_install"
# after_install = "production_operations.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "production_operations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
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
# 		"production_operations.tasks.all"
# 	],
# 	"daily": [
# 		"production_operations.tasks.daily"
# 	],
# 	"hourly": [
# 		"production_operations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"production_operations.tasks.weekly"
# 	]
# 	"monthly": [
# 		"production_operations.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "production_operations.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "production_operations.event.get_events"
# }