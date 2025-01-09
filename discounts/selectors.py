from .models import Discount


def discount_list_display():
    discount = Discount.objects.all().filter(is_active=True).order_by("created_at")
    return discount


def discount_detail_display(discount_id):
    discount = Discount.objects.get(id=discount_id)
    return discount
