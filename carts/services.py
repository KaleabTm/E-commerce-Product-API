from django.shortcuts import get_object_or_404
from carts.models import Cart, CartItem
from carts.selectors import get_cart
from discounts.services import apply_discount
from products.models import Products
from django.contrib.auth import get_user_model

User = get_user_model()


def create_cart(
    *,
    user,
) -> Cart:
    print("launched carti item create")
    u = get_object_or_404(User, email=user)
    print("got user", u)
    cart = Cart.objects.create(user=u)

    print("cart",cart)

    cart.full_clean()

    cart.save()

    return cart


def add_to_cart(user, product, quantity):
    cart = get_cart(user)
    products = get_object_or_404(Products, id=product)

    if products.stock < quantity:
        raise ValueError("Insufficient stock available.")

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=products, quantity=quantity)

    cart_item.cart_item_total_price = apply_discount(products.id) * quantity

    cart_item.save()

    return cart_item


def update_cart_item_quantity(user, cart_item_id, product_id, quantity):
    cart = get_object_or_404(Cart, user=user)
    product = get_object_or_404(Products, id=product_id)

    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.quantity = quantity
    cart_item.save()

    return cart_item


def remove_cart_item(cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()

    return None
