from django.urls import path
from .apis import Login, Logout, RegisterApi

app_name = "authentication"

urlpatterns = [
    path("login/", Login.as_view(), name="user-login"),
    path("logout/", Logout.as_view(), name="user-logout"),
    path("register/", RegisterApi.as_view(), name="user-register"),
]
