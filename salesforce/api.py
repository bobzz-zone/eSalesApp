from __future__ import unicode_literals
import frappe
import json
import time
import datetime
import os

@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

@frappe.whitelist(allow_guest=False)
def get_metadata():
	data = dict()

	#sales order
	status = ['Draft', 'To Deliver and Bill','To Bill','To Deliver','Completed','Cancelled','Closed']
	data['sales_order'] = dict()
	dataSO = data['sales_order']
	dataSO['count'] = dict()
	dataCount = dataSO['count']
	for stat in status:
		fetch = frappe.db.sql("SELECT COUNT(name) FROM `tabSales Order` WHERE docstatus = 1 AND status='{}' ORDER BY modified".format(stat),as_list=1)
		if (len(fetch) > 0):
			firstFetch = fetch[0]
			dataCount[stat] = firstFetch[0]

	#invoice
	status = ['Overdue','Unpaid','Paid']
	data['invoice'] = dict()
	dataINV = data['invoice']
	dataINV['count'] = dict()
	dataCount = dataINV['count']
	for stat in status:
		fetch = frappe.db.sql("SELECT COUNT(name) FROM `tabSales Invoice` WHERE docstatus = 1 AND status='{}' ORDER BY modified".format(stat),as_list=1)
		if (len(fetch) > 0):
			firstFetch = fetch[0]
			dataCount[stat] = firstFetch[0]

	#lead
	status = ['Lead','Open','Replied','Opportunity','Interested','Quotation','Lost Quotation','Converted','Do Not Contact']
	data['lead'] = dict()
	dataLead = data['lead']
	dataLead['count'] = dict()
	dataCount = dataLead['count']
	for stat in status:
		fetch = frappe.db.sql("SELECT COUNT(name) FROM `tabLead` WHERE status='{}' ORDER BY modified".format(stat),as_list=1)
		if (len(fetch) > 0):
			firstFetch = fetch[0]
			dataCount[stat] = firstFetch[0]

	#net sales
	fetchNetSales = frappe.db.sql("SELECT SUM(grand_total) as net_sales, posting_date FROM `tabSales Invoice` WHERE status='Paid' GROUP BY posting_date",as_dict=1)
	data['daily_net_sales'] = fetchNetSales

	return data


@frappe.whitelist(allow_guest=False)
def get_sales_order(status='',query='',sort='',page=0):
	filters = ['name','customer_name']
	n_filters = len(filters)
	generate_filters = ""
	for i in range(0,n_filters-1):
		generate_filters += "{} LIKE '%{}%' OR ".format(filters[i],query)
	generate_filters += "{} LIKE '%{}%' ".format(filters[n_filters-1],query)

	statuses = status.split(',')
	generate_status = "'" + "','".join(statuses) + "'"

	sortedby = 'modified'
	if (sort != ''):
		sortedby = sort

	data = frappe.db.sql("SELECT * FROM `tabSales Order` WHERE docstatus = 1 AND status IN ({}) AND ({}) ORDER BY {} DESC, status ASC LIMIT 20 OFFSET {}".format(generate_status,generate_filters,sortedby,page),as_dict=1)

	return data

@frappe.whitelist(allow_guest=False)
def get_sales_invoice(status='',query='',sort='',page=0):
	filters = ['name','customer_name']
	n_filters = len(filters)
	generate_filters = ""
	for i in range(0,n_filters-1):
		generate_filters += "{} LIKE '%{}%' OR ".format(filters[i],query)
	generate_filters += "{} LIKE '%{}%' ".format(filters[n_filters-1],query)

	statuses = status.split(',')
	generate_status = "'" + "','".join(statuses) + "'"

	sortedby = 'modified'
	if (sort != ''):
		sortedby = sort

	data = frappe.db.sql("SELECT * FROM `tabSales Invoice` WHERE docstatus = 1 AND status IN ({}) AND ({}) ORDER BY {} DESC, status ASC LIMIT 20 OFFSET {}".format(generate_status,generate_filters,sortedby,page),as_dict=1)

	return data

@frappe.whitelist(allow_guest=False)
def get_item(is_sales_item='1',is_stock_item='1',ref='',page='0'):
	data = frappe.db.sql("SELECT * FROM `tabItem` WHERE is_sales_item = {} AND is_stock_item = {} AND (item_name LIKE '{}%' OR item_code LIKE '{}%') LIMIT 20 OFFSET {}".format(is_sales_item, is_stock_item,ref,ref,page),as_dict=1)

	for row in data:
		row['product_bundle_item'] = list("")
		if (row['is_stock_item'] == 0):
			fetchBundleItem = frappe.db.sql("SELECT * FROM `tabProduct Bundle Item` WHERE parent = '{}'".format(row['item_code']),as_dict=True)
			row['product_bundle_item'] = fetchBundleItem
	return data

@frappe.whitelist(allow_guest=False)
def get_lead(status='',query='',sort='',page=0):
	filters = ['name','company_name','lead_name','email_id']
	n_filters = len(filters)
	generate_filters = ""
	for i in range(0,n_filters-1):
		generate_filters += "{} LIKE '%{}%' OR ".format(filters[i],query)
	generate_filters += "{} LIKE '%{}%' ".format(filters[n_filters-1],query)

	statuses = status.split(',')
	generate_status = "'" + "','".join(statuses) + "'"

	sortedby = 'modified'
	if (sort != ''):
		sortedby = sort

	data = frappe.db.sql("SELECT * FROM `tabLead` WHERE status IN ({}) AND ({}) ORDER BY {} DESC, status ASC LIMIT 20 OFFSET {}".format(generate_status,generate_filters,sortedby,page),as_dict=1)

	return data

@frappe.whitelist(allow_guest=False)
def get_lead_item(lead_no=''):
	fetch_opportunity = frappe.db.sql("SELECT * FROM `tabOpportunity` WHERE lead = '{}'".format(lead_no),as_dict=1)
	fetch_quotation = frappe.db.sql("SELECT * FROM `tabQuotation` WHERE lead = '{}'".format(lead_no),as_dict=1)
	data = dict()
	data['opportunity'] = fetch_opportunity
	data['quotation'] = fetch_quotation
	return data

