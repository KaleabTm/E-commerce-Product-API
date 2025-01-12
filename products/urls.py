from django.urls import path
from .apis import (
    ProductCreateApi,
    ProductListApi,
    ProductDetailApi,
    ProductUpdateApi,
    ProductSearchApi,
)

app_name = "products"

urlpatterns = [
    path("create/", ProductCreateApi.as_view(), name="create-product"),
    path("list/", ProductListApi.as_view(), name="list-product"),
    path("<uuid:id>/update/", ProductUpdateApi.as_view(), name="update-product"),
    path("<uuid:id>/detail/", ProductDetailApi.as_view(), name="detail-product"),
    path("search/", ProductSearchApi.as_view(), name="search-product"),
]
