from rules import predicate


@predicate
def is_staff(user):
    return user.is_staff


@predicate
def is_superuser(user):
    return user.is_superuser


@predicate
def is_cart_owner(user, cart):
    return cart.user == user


@predicate
def is_customer(user):
    return not user.role == "CU"


@predicate
def is_authenticated(user):
    return user.is_authenticated


@predicate
def is_admin(user):
    return user.role == "AD"


@predicate
def is_reviewer(user, review):
    return review.user == user


@predicate
def order_owner(user, order):
    return order.user == user
