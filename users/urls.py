from django.urls import path

from .apis import UserCreateApi, UserUpdateApi

app_name = "users"

urlpatterns = [
    path('create/', UserCreateApi.as_view(),name="create-user"),
    path('<uuid:id>/update/', UserUpdateApi.as_view(),name="update-user"),
    path('<uuid:id>/delete/', UserUpdateApi.as_view(),name="create-user"),
]
