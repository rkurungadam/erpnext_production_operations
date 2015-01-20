# erpnext_production_operations
Extends Manufacturing Module of ERPNEXT
- This app creates Production Operations as specified in BoM on submit of Production Orders 
- Lists Raw Materials(exploded) to be used in each operation
- Timesheets entry for Operations
- All Operations for an Order have to be marked complete before Updating Finished Goods

Depends
- frappe/erpnext https://github.com/frappe/bench

Installation
- bench get-app production_operations https://github.com/rkurungadam/erpnext_production_operations.git
- bench frappe --install_app production_operations your_site_name 
  or 
  use frappe desk installer module
