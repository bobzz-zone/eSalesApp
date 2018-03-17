# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "salesforce"
app_title = "Sales Force"
app_publisher = "Bobby Hartanto"
app_description = "For Sales Force Application"
app_icon = "octicon octicon-checklist"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/salesforce/css/salesforce.css"
# app_include_js = "/assets/salesforce/js/salesforce.js"

# include js, css files in header of web template
# web_include_css = "/assets/salesforce/css/salesforce.css"
# web_include_js = "/assets/salesforce/js/salesforce.js"

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
# get_website_user_home_page = "salesforce.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "salesforce.install.before_install"
# after_install = "salesforce.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "salesforce.notifications.get_notification_config"

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
# 		"salesforce.tasks.all"
# 	],
# 	"daily": [
# 		"salesforce.tasks.daily"
# 	],
# 	"hourly": [
# 		"salesforce.tasks.hourly"
# 	],
# 	"weekly": [
# 		"salesforce.tasks.weekly"
# 	]
# 	"monthly": [
# 		"salesforce.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "salesforce.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "salesforce.event.get_events"
# }

