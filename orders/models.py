from django.db import models
from products.models import Products
from common.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(BaseModel):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        CANCELLED = "CANCELLED", "Cancelled"
        DELIVERED = "DELIVERED", "Delivered"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(
        max_length=15, choices=Status.choices, default=Status.PENDING
    )
    has_paid = models.BooleanField(default=False)

    @property
    def order_total_price(self):
        return sum(item.total_price for item in self.items.all())

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order {self.id} by {self.user.email} - with total price of {self.total_price}  - {self.status} - {self.has_paid} "


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Products, on_delete=models.PROTECT, related_name="order_items"
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_total_price = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order #{self.order.id}"
