from django.contrib.auth import get_user_model


User = get_user_model()


def create_user(
    *,
    email,
    password,
    first_name,
    last_name,
    phone_number,
    address,
    profile_pic,
    date_of_birth,
    role="CU"
):
    user = User.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        address=address,
        profile_pic=profile_pic,
        date_of_birth=date_of_birth,
        role=role
    )

    user.full_clean()
    user.save()

    return user


def update_userprofile(
    *,
    user_id,
    email=None,
    password=None,
    first_name=None,
    last_name=None,
    phone_number=None,
    address=None,
    profile_pic=None,
    date_of_birth=None,
):
    user = User.objects.get(id=user_id)
    if first_name is not None:
        user.first_name = first_name
    if last_name is not None:
        user.last_name = last_name
    if phone_number is not None:
        user.phone_number = phone_number
    if address is not None:
        user.address = address
    if email is not None:
        user.email = email
    if password is not None:
        user.set_password(password)  # Ensure the password is hashed
    if profile_pic is not None:
        user.profile_pic = profile_pic
    if date_of_birth is not None:
        user.date_of_birth = date_of_birth

    user.full_clean()
    user.save()

    return user


def delete_user(
    *,
    user,
):
    user.delete()

    return None
