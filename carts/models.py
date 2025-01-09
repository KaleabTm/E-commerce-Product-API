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
    product = models.ForeignKey(
        "products.Products", on_delete=models.CASCADE, related_name="cart_items"
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"


class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlists")
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="wishlists"
    )

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user} - {self.product.product_name}"
