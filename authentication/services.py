from django.contrib.auth import get_user_model

User = get_user_model()



def create_user(
    *,
    email: str,
    password: str,
):
    print(f"Creating user with email: {email} and password: {password}") 
    return User.objects.create_user(
        email=email,
        password=password
    )
