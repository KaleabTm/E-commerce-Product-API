from django.contrib.auth import get_user_model
from .models import Products
from category.models import Category

User = get_user_model()


def create_product(
    *,
    name: str,
    description: str,
    price: float,
    created_by: str,
    stock: int,
    category: str,
) -> Products:
    u = User.objects.get(email=created_by)
    c = Category.objects.get(id=category)
    p = Products.objects.create(
        name=name,
        description=description,
        price=price,
        created_by=u,
        category=c,
        stock=stock,
    )

    p.full_clean()

    p.save()

    return p


def create_product_image(*, product: str, image, label: str) -> Products:
    p = Products.objects.get(id=product)
    pi = Products.objects.create(product=p, image=image, label=label)

    pi.full_clean()

    pi.save()

    return pi
