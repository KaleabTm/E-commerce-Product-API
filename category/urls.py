from django.urls import path
from .apis import (
    CategoryCreateView,
    CategoryListView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryUpdateView,
)

app_name = "category"

urlpatterns = [
    path("", CategoryListView.as_view(), name="list-category"),
    path("create/", CategoryCreateView.as_view(), name="create-category"),
    path(
        "<uuid:category_id>/detail/",
        CategoryDetailView.as_view(),
        name="detail-category",
    ),
    path(
        "<uuid:category_id>/update/",
        CategoryUpdateView.as_view(),
        name="update-category",
    ),
    path(
        "<uuid:category_id>/delete/",
        CategoryDeleteView.as_view(),
        name="delete-category",
    ),
]
