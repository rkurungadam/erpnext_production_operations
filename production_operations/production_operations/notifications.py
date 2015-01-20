from __future__ import unicode_literals
import frappe

def get_notification_config():
	return { "for_doctype": 
		{
			"Production Operations": {"status":"Pending"},
		}
	}