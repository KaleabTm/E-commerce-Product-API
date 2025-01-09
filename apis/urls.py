from django.urls import path, include

app_name = "apis"
urlpatterns = [
    path("auth/", include("authentication.urls", namespace="authentication")),
    path("carts/", include("carts.urls", namespace="carts")),
    path("category/", include("category.urls", namespace="category")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("products/", include("products.urls", namespace="products")),
    path("users/", include("users.urls", namespace="users")),
    path("discounts/", include("discounts.urls", namespace="discounts")),
]
