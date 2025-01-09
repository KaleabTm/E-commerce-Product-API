# Register your models here.
from django.contrib import admin

from .models import ProductImage, Products


admin.site.register(ProductImage)
admin.site.register(Products)