from django.db.models import QuerySet
from .models import Products  # Adjust this import based on your app structure


def product_list() -> QuerySet[Products]:
    products = Products.objects.prefetch_related("images").all().order_by("created_at")

    return products


def product_detail(id) -> Products:
    product = Products.objects.prefetch_related("images").get(id=id)

    return product
