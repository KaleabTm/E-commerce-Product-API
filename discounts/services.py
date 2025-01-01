from products.models import Products
from .models import Discount


def create_discount(
    *,
    product,
    discount_type,
    value,
    start_date,
    end_date,
) -> Discount:
    if start_date > end_date:
        raise ValueError("Start date cannot be greater than end date.")

    if end_date < start_date:
        raise ValueError("End date cannot be befor start date.")

    discount = Discount.objects.create(
        product=product,
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


def discounted_price(id):
    product = Products.objects.get(id=id)
    discount = Discount.objects.filter(product=product)

    if not discount.is_active():
        return product.product_price

    if discount.discount_type == "PERCENTAGE":
        return product.product_price * (1 - discount.value / 100)
    elif discount.discount_type == "FLAT":
        return product.product_price - discount.value

    return product.product_price
