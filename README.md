# erpnext_production_operations
Extends Manufacturing Module of ERPNEXT
- This app creates Production Operations(new entity) corresponding to operations specified in the BoM on submit of Production Order
- Lists Raw Materials(exploded) to be used in each Production Operation
- User assignments, Timesheet entry for Operations
- Update Finished Goods of Production Order requires all Production Operations of the Order to be marked complete

Depends
- frappe/erpnext https://github.com/frappe/bench

Installation
- bench get-app production_operations https://github.com/rkurungadam/erpnext_production_operations.git
- bench frappe --install_app production_operations your_site_name 
  or 
  use frappe desk installer module
