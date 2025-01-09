from django.db.models import Q
from .models import Products

def filter_products(query=None, category=None):
    queryset = Products.objects.all()

    if query:
        queryset = queryset.filter(Q(name__icontains=query))
    if category:
        queryset = queryset.filter(category__name__icontains=category)  # Assuming category is a FK.

    return queryset
