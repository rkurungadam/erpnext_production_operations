# Copyright (c) 2013, earthians and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import cstr, flt, today

class ProductionOperations(Document):

	def set_in_progress(self):
		frappe.db.set(self, 'status', 'In Progress')
		frappe.db.set(self, 'start_date', today())

	def set_complete(self):
		frappe.db.set(self, 'status', 'Complete')
		frappe.db.set(self, 'end_date', today())
		frappe.db.set(self, 'docstatus', 1)

	def set_pending(self):
		frappe.db.set(self, 'status', 'Pending')

	def set_cancel(self):
		frappe.db.set(self, 'status', 'Cancel')
		frappe.db.set(self, 'docstatus', 2)

	def validate(self):
		self.update_spent_time()

	def update_spent_time(self):
		amount = 0
		for d in self.get('op_timesheet'):
			amount += d.minutes
		self.spent_time = amount


def create_operations(doc, method):	
	bom = doc.get('bom_no')
	bom_obj = frappe.get_doc('BOM', bom)
	item = doc.get('production_item')
	qty = doc.get('qty')
	uom = doc.get('stock_uom')
	description= doc.get('description')
	bom_ops = bom_obj.get('bom_operations')
	#creare production operations from bom operations
	for op in bom_ops:
		production_op = frappe.new_doc('Production Operations')
		production_op.op_name = op.operation_no
		production_op.op_desc = op.opn_description
		production_op.workstation = op.workstation
		production_op.planned_time = op.time_in_mins
		production_op.item = item
		production_op.qty = qty
		production_op.item_desc = description
		production_op.uom = uom
		production_op.p_order = doc.name
		production_op.bom = bom

		#fetch items required for each operation and add raw material lines
		material_dict = frappe.db.sql("""select bom_no, qty_consumed_per_unit, item_code, stock_uom  from `tabBOM Item`
			where operation_no=%s""", op.operation_no, as_dict=1)
		for material in material_dict:
			#if raw material has BOM, fetch and add the exploded items
			if material.bom_no and doc.use_multi_level_bom:
				from erpnext.manufacturing.doctype.bom.bom import get_bom_items_as_dict
				exploded_items = get_bom_items_as_dict(material.bom_no, qty=qty*material.qty_consumed_per_unit, fetch_exploded = 1)
				for d in exploded_items:
					line = production_op.append('raw_materials')
					line.item_code = cstr(d)
					line.item_qty = flt(exploded_items[d]["qty"])
					line.uom = exploded_items[d]["stock_uom"]
			else:
				line = production_op.append('raw_materials')
				line.item_code = material.item_code
				line.item_qty = qty*material.qty_consumed_per_unit
				line.uom = material.stock_uom

		production_op.save()

def cancel_operations(doc, method):
	operations = frappe.db.get_values("Production Operations", {"p_order": doc.name}, "name", as_dict=1)
	if operations:
		for op in operations:
			op_obj = frappe.get_doc('Production Operations', op)
			op_obj.set_cancel()


@frappe.whitelist()
def validate_operations(production_order_id, purpose, qty=None):
	from erpnext.manufacturing.doctype.production_order.production_order import make_stock_entry
	production_order = frappe.get_doc("Production Order", production_order_id)
	bom = frappe.get_doc("BOM", production_order.bom_no)	
	if not bom.with_operations or purpose == "Material Transfer":
		return make_stock_entry(production_order_id, purpose, qty=None)
	ops = frappe.db.sql("""select status from `tabProduction Operations` where p_order=%s""", production_order_id, as_dict=1)
	for d in ops:
		if d.status != "Complete":
			frappe.throw(_("Please Complete all Production Operations of this Order"))
	return make_stock_entry(production_order_id, purpose, qty=None)