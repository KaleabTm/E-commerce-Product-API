from django.contrib.auth import get_user_model


User = get_user_model()


def create_use(
    *,
    email,
    password,
    first_name,
    last_name,
    phone_number,
    address,
    city,
    country,
    postal_code,
):
    user = User.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        address=address,
        city=city,
        country=country,
        postal_code=postal_code,
    )

    user.full_clean()
    user.save()

    return user


def update_userprofile(
    *,
    user,
    first_name,
    last_name,
    phone_number,
    address,
    city,
    country,
    postal_code,
):
    user.first_name = first_name
    user.last_name = last_name
    user.phone_number = phone_number
    user.address = address
    user.city = city
    user.country = country
    user.postal_code = postal_code

    user.full_clean()
    user.save()

    return user


def delete_user(
    *,
    user,
):
    user.delete()

    return None
