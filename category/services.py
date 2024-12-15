from .models import Category


def create_category(
        *,
        name:str,
        description:str
)->Category:
    c = Category.objects.create(
        name=name,
        description=description
    )

    c.full_clean()

    c.save()

    return c