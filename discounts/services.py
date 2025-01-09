from products.models import Products
from .models import Discount


from django.utils.timezone import now


def create_discount(
    *,
    product,
    discount_type,
    value,
    start_date,
    end_date,
) -> Discount:
    products = Products.objects.get(id=product)
    

    if start_date > end_date:
        raise ValueError("Start date cannot be greater than end date.")

    if end_date < start_date:
        raise ValueError("End date cannot be befor start date.")

    discount = Discount.objects.create(
        product=products,
        discount_type=discount_type,
        value=value,
        start_date=start_date,
        end_date=end_date,
    )

    discount.full_clean()

    discount.save()

    return discount


def update_discount(
    *,
    discount,
    discount_type,
    value,
    start_date,
    end_date,
) -> Discount:
    if start_date > end_date:
        raise ValueError("Start date cannot be greater than end date.")

    if end_date < start_date:
        raise ValueError("End date cannot be befor start date.")

    discount.discount_type = discount_type
    discount.value = value
    discount.start_date = start_date
    discount.end_date = end_date

    discount.full_clean()

    discount.save()

    return discount


def delete_discount(
    *,
    discount,
) -> Discount:
    discount.delete()

    return None

def is_available(discount):
    return discount.start_date <= now() <= discount.end_date

def apply_discount(product_id):
    product = Products.objects.get(id=product_id)
    discount = Discount.objects.filter(product=product).first()

    if not discount:
        return product.price

    if is_available(discount):
        if discount.discount_type == "PERCENTAGE":
            return product.price * (1 - discount.value / 100)
        elif discount.discount_type == "FLAT":
            return product.price - discount.value

    return product.price


def deactivate_discount(discount_id):
    discount = Discount.objects.get(id=discount_id)
    discount.is_active = False
    discount.save()

    return discount


def reactivate_discount(discount_id, start_date, end_date):
    discount = Discount.objects.get(id=discount_id)
    if start_date > end_date:
        raise ValueError("Start date cannot be greater than end date.")
    if start_date < now():
        raise ValueError("Start date cannot be in the past.")
    
    discount.start_date = start_date
    discount.end_date = end_date
    discount.is_active = True

    discount.save()

    return discount

