from django.urls import path
from .apis import DiscountCreateApi, DiscountUpdateApi, DiscountReactivateApi, DiscountDeactivateApi, DiscountListApi, DiscountDetailApi

app_name = "discounts"

urlpatterns = [
    path('', DiscountListApi.as_view(),name="discount-list"),
    path('create/', DiscountCreateApi.as_view(),name="discount-create"),
    path('<uuid:id>/reactivate/', DiscountReactivateApi.as_view(),name="discount-reactivate"),
    path('<uuid:id>/deactivate/', DiscountDeactivateApi.as_view(),name="discount-deactivate"),
    path('<uuid:id>/detail/', DiscountDetailApi.as_view(),name="discount-detail"),
    path('<uuid:id>/update/', DiscountUpdateApi.as_view(),name="discount-update"),
]