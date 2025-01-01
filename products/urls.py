from django.urls import path
from .apis import ProductCreateView, ProductListView

app_name = "products"

urlpatterns = [
    path("create/", ProductCreateView.as_view(), name="create-product"),
    path("list/", ProductListView.as_view(), name="list-product"),
]
