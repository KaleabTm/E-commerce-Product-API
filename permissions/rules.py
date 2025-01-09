import rules
from .predicates import is_admin, is_superuser, is_staff, is_customer, is_authenticated, is_cart_owner, is_reviewer, order_owner


rules.add_perm('add_user', is_superuser | is_staff | is_admin)
rules.add_perm('delete_user', is_superuser | is_staff | is_admin)
rules.add_perm('update_user', is_superuser | is_staff | is_admin) 

rules.add_perm('add_product', is_superuser | is_staff | is_admin)
rules.add_perm('delete_product', is_superuser | is_admin)
rules.add_perm('update_product', is_superuser | is_staff | is_admin)
rules.add_perm('view_product', is_authenticated | is_customer | is_staff | is_admin | is_superuser)

rules.add_perm('add_cart_item', is_cart_owner)
rules.add_perm('delete_cart_item', is_cart_owner)
rules.add_perm('update_cart_item', is_cart_owner)
rules.add_perm('view_cart_item', is_cart_owner)

rules.add_perm('create_review', is_authenticated, is_customer)
rules.add_perm('delete_review', is_reviewer)
rules.add_perm('update_review', is_reviewer)
rules.add_perm('view_review', is_authenticated | is_customer | is_staff | is_admin | is_superuser | is_reviewer)

rules.add_perm('create_discount', is_admin | is_superuser)
rules.add_perm('delete_discount', is_admin | is_superuser)
rules.add_perm('update_discount', is_admin | is_superuser)
rules.add_perm('view_discount', is_authenticated | is_customer | is_staff | is_admin | is_superuser)

rules.add_perm('create_order', is_authenticated | is_customer)
rules.add_perm('delete_order', order_owner)
rules.add_perm('update_order', order_owner)
rules.add_perm('view_order', order_owner | is_admin | is_superuser)
rules.add_perm('approve_order', is_admin | is_superuser)

