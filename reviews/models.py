from django.db import models

from common.models import BaseModel
from products.models import Products
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class Rating(BaseModel):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="ratings"
    )
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.rating} for {self.product.name}"


class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.ForeignKey(Rating, on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Review by {self.user} on {self.product.name} - {self.rating}/5"
