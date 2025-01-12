from django.urls import path
from .apis import (
    PlaceOrderApi,
    PlaceOrderCartApi,
    OrderCancelApi,
    OrderUpdateApi,
    OrderApproveApi,
    PlaceOrderCartAllApi,
    OrderItemListViewApi,
    OrderItemDetailViewApi,
)

app_name = "orders"

urlpatterns = [
    path("create/", PlaceOrderApi.as_view(), name="place_order"),
    path("order_cart/", PlaceOrderCartApi.as_view(), name="place_order_from_cart"),
    path("<uuid:order_id>/cancel/", OrderCancelApi.as_view(), name="cancel_order"),
    path("<uuid:id>/update/", OrderUpdateApi.as_view(), name="update_order"),
    path("<uuid:id>/approve/", OrderApproveApi.as_view(), name="approve_order"),
    path(
        "order_cart/all/",
        PlaceOrderCartAllApi.as_view(),
        name="place_order_from_all_cart_items",
    ),
    path("", OrderItemListViewApi.as_view(), name="order_item_list"),
    path(
        "<uuid:id>/detail", OrderItemDetailViewApi.as_view(), name="order_item_detail"
    ),
]
