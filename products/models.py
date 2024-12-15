from django.db import models
from common.models import BaseModel
from category.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Products(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return f"{self.name} - {self.category} - {self.price}"
