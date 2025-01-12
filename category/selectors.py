from .models import Category


def category_list():
    return Category.objects.all()


def category_detail(category_id):
    return Category.objects.get(id=category_id)
