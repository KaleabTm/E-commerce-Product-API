from django.forms import ValidationError
from django.shortcuts import get_object_or_404

from carts.models import Cart
from .models import OrderItem, Order
from django.contrib.auth import get_user_model
from products.models import Products

User = get_user_model()


def create_order(*, user, has_paid=False, status="PENDING") -> Order:
    customer = get_object_or_404(User, email=user)
    order = Order.objects.create(user=customer, has_paid=has_paid, status=status)

    order.full_clean()

    order.save()

    return order


def create_order_item(*, order, user, product: str, quantity: int) -> OrderItem:
    orders = create_order(user)
    target_product = []
    for product in product:
        if target_product.stock < quantity:
            raise ValueError(f"Not enough stock for {product.name}")
        target_product = get_object_or_404(Products, id=product)

        target_product.stock -= quantity

        item_total_price = target_product.price * quantity

    order_item = OrderItem.objects.create(
        order=orders,
        product=target_product,
        quantity=quantity,
        price=target_product.price,
        item_total_price=item_total_price,
    )

    for total_price in item_total_price:
        orders.order_total_price += total_price

        orders.save()

    order_item.full_clean()

    order_item.save()


def approve_order(order_id):
    order = get_object_or_404(Order, id=order_id)
    if not order.has_paid:
        raise ValidationError("Order cannot be approved without payment.")
    order.status = Order.Status.APPROVED
    order.save()


def deliver_order(order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.status != Order.Status.APPROVED:
        raise ValidationError("Order must be approved before being delivered.")
    order.status = Order.Status.DELIVERED
    order.save()


def place_order_cart(user):
    cart = Cart.objects.prefetch_related("items").get(user=user)
    items = cart.items.all()
    total_amount = sum(item.total_price() for item in items)

    # Create the order
    order = Order.objects.create(user=user, total_amount=total_amount, status="Pending")

    # Create order items and reduce stock
    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )
        item.product.reduce_stock(item.quantity)

    # Clear the cart after order
    cart.items.all().delete()
    return order
