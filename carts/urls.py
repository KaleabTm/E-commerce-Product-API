from django.urls import path
from .apis import CartItemCreateApi, CartItemDeleteApi, CartItemListSerializer, CartItemUpdateApi, CartItemDetailViewApi

app_name = "carts"

urlpatterns = [
    path('', CartItemListSerializer, name="cart-list"),
    path('create/', CartItemCreateApi.as_view(), name="cart-create"),
    path('<uuid:id>/update/', CartItemUpdateApi.as_view(), name="cart-update"),
    path('<uuid:id>/delete/', CartItemDeleteApi.as_view(), name="cart-delete"),
    path('<uuid:id>/detail', CartItemDetailViewApi.as_view(), name="cart-detail"),
]
