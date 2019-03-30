# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from calendar import monthrange

def execute(filters=None):
	conditions, filters = get_conditions(filters)
	columns = get_column()
	data = get_data(conditions,filters)
	return columns,data

def get_column():
	return [_("Date") + ":Date:90",_("Category") + ":Data:90",_("Subcategory") + ":Data:110",_("Size") + ":Data:90",_("Color") + ":Data:105",_("Sales Invoice") + ":Data:110",_("Qty") + ":Float:105",_("Rate") + ":Float:105",_("Discount %") + ":Float:105"]

def get_data(conditions,filters):
	sales = frappe.db.sql("""SELECT si.posting_date, i.item_group, SUBSTRING_INDEX(i.item_name, '-', 1),SUBSTRING_INDEX(SUBSTRING_INDEX(i.item_name, '-', 2), '-', -1),SUBSTRING_INDEX(i.item_name, '-', -1), si.name, i.qty, i.rate, i.discount_percentage from `tabSales Invoice Item` i, `tabSales Invoice` si where si.name = i.parent and status != 'Cancelled' %s;""" %conditions,filters, as_list=1)
	return sales

def get_conditions(filters):
	conditions = ""
	filters["month"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
		"Dec"].index(filters.month) + 1
	conditions += " and month(si.posting_date) = %(month)s"

	return conditions, filters
