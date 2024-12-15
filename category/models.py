from django.db import models
from common.models import BaseModel


# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"
