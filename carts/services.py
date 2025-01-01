from django.shortcuts import get_object_or_404
from carts.models import Cart, CartItem
from products.models import Products
from django.contrib.auth import get_user_model

User = get_user_model()


def create_cart(
    *,
    user,
) -> Cart:
    u = get_object_or_404(User, email=user)
    cart = Cart.objects.create(user=u)

    cart.full_clean()

    cart.save()

    return cart


def add_to_cart(user, product_id, quantity):
    cart, _ = Cart.objects.get(user=user)
    product = get_object_or_404(Products, id=product_id)

    if product.stock < quantity:
        raise ValueError("Insufficient stock available.")

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()

    return cart_item


def update_cart_item_quantity(user, product_id, quantity):
    cart = get_object_or_404(Cart, user=user)
    product = get_object_or_404(Products, id=product_id)

    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.quantity = quantity
    cart_item.save()

    return cart_item


def remove_cart_item(user, product_id):
    cart = get_object_or_404(Cart, user=user)
    product = get_object_or_404(Products, id=product_id)

    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()

    return cart_item
