from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("MIS Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Profit and Loss Statement",
					"doctype": "GL Entry"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Balance",
					"doctype": "Stock Ledger Entry"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Ledger",
					"doctype": "Stock Ledger Entry"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Total Stock Summary",
					"doctype": "Stock Entry"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Item-wise Sales Register",
					"doctype": "Sales Invoice"
				}
			]
		},
		{
			"label": _("Sales Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales Report for the stores",
					"doctype": "Sales Invoice"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales report for the Management",
					"doctype": "Sales Invoice"
				}
			]
		}
	]
