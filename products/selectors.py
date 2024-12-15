from django.db.models import QuerySet
from .models import Products  # Adjust this import based on your app structure

def product_list() -> QuerySet[Products]:
    products = Products.objects.all().order_by('created_at')
    
    return products