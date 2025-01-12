from django.urls import path

from .apis import UserCreateApi, UserUpdateApi, UserDetailApi, UserListApi

app_name = "users"

urlpatterns = [
    path("create/", UserCreateApi.as_view(), name="create-user"),
    path("<uuid:id>/update/", UserUpdateApi.as_view(), name="update-user"),
    path("<uuid:id>/detail/", UserDetailApi.as_view(), name="detail-user"),
    path("list/", UserListApi.as_view(), name="list-user"),
]
