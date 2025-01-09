from .models import Category
from django.shortcuts import get_object_or_404

def create_category(*, name: str, description: str) -> Category:
    category = Category.objects.create(name=name, description=description)

    category.full_clean()

    category.save()

    return category

def update_category(*, category_id, name: str, description: str) -> Category:
    category = get_object_or_404(Category, id=category_id)
    category.name = name
    category.description = description

    category.full_clean()

    category.save()

    return category


def delete_category(*, category_id) -> Category:
    category = get_object_or_404(Category, id=category_id)
    category.delete()

    return None
