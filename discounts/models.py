from django.db import models
from django.utils.timezone import now
from common.models import BaseModel
from products.models import Products


class Discount(BaseModel):
    class DiscountType(models.TextChoices):
        PERCENTAGE = "PERCENTAGE", "Percentage"
        FLAT = "FLAT", "Flat Discount"

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name="discounts",
        null=True,
        blank=True,
    )
    discount_type = models.CharField(max_length=20, choices=DiscountType.choices)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.product:
            return (
                f"{self.discount_type} Discount on {self.product.name} - {self.value}"
            )
        return f"{self.discount_type} Discount on {self.product.category.name} - {self.value}"
