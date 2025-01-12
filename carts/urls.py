from django.urls import path
from .apis import (
    CartItemCreateApi,
    CartItemDeleteApi,
    CartItemListViewApi,
    CartItemUpdateApi,
    CartItemDetailViewApi,
)

app_name = "carts"

urlpatterns = [
    path("", CartItemListViewApi.as_view(), name="cart-list"),
    path("create/", CartItemCreateApi.as_view(), name="cart-create"),
    path("<uuid:id>/update/", CartItemUpdateApi.as_view(), name="cart-update"),
    path("<uuid:id>/delete/", CartItemDeleteApi.as_view(), name="cart-delete"),
    path("<uuid:id>/detail/", CartItemDetailViewApi.as_view(), name="cart-detail"),
]
