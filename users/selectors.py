from django.db.models import QuerySet
from .models import Users  


def user_list() -> Users:
    users = Users.objects.all()

    return users


def user_detail(id) -> Users:
    product = Users.objects.get(id=id)

    return product
