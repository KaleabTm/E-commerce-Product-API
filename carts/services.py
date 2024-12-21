from django.shortcuts import get_object_or_404
from carts.models import Cart, CartItem
from products.models import Products
from django.contrib.auth import get_user_model

User = get_user_model()

def create_cart(
        *,
        user,
)->Cart:
    u = get_object_or_404(User, email=user)
    cart = Cart.objects.get_or_create(u)

    cart.full_clean()

    cart.save()

    return cart


def add_to_cart(user, product_id, quantity):
    cart, _ = Cart.objects.get_or_create(user=user)
    product = get_object_or_404(Products,id=product_id)

    if product.stock < quantity:
        raise ValueError("Insufficient stock available.")

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()
    
    return cart_item
