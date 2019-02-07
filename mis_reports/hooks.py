# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mis_reports"
app_title = "Mis Reports"
app_publisher = "Hardik Gadesha"
app_description = "App to show all reports"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "hardikgadesha@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mis_reports/css/mis_reports.css"
# app_include_js = "/assets/mis_reports/js/mis_reports.js"

# include js, css files in header of web template
# web_include_css = "/assets/mis_reports/css/mis_reports.css"
# web_include_js = "/assets/mis_reports/js/mis_reports.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mis_reports.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mis_reports.install.before_install"
# after_install = "mis_reports.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mis_reports.notifications.get_notification_config"

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
# 		"mis_reports.tasks.all"
# 	],
# 	"daily": [
# 		"mis_reports.tasks.daily"
# 	],
# 	"hourly": [
# 		"mis_reports.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mis_reports.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mis_reports.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mis_reports.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mis_reports.event.get_events"
# }

