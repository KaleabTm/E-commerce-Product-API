from .models import Order, OrderItem


def order_item_detail(id):
    return OrderItem.objects.get(id=id)


def get_order(user):
    return Order.objects.prefetch_related("items").filter(user=user)


def order_item_list(order):
    return OrderItem.objects.filter(order=order)
