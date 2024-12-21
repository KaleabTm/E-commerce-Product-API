
from datetime import timezone
from django.db import models

from common.models import BaseModel

from products.models import Products
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")

    def __str__(self):
        return f"{self.id} - cart of {self.user.email}"



class CartItem(BaseModel):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Products", on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField()

    @property
    def discounted_price(self):
        active_discount = self.product.discounts.filter(
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now(),
        ).first()
        if active_discount:
            if active_discount.discount_type == "PERCENTAGE":
                return self.product.product_price * (1 - active_discount.value / 100)
            elif active_discount.discount_type == "FLAT":
                return self.product.product_price - active_discount.value
        return self.product.product_price

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"




class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlists")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="wishlists")

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user} - {self.product.product_name}"
