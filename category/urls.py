from django.urls import path
from .apis import CategoryCreateView

app_name = "category"

urlpatterns = [path("create/", CategoryCreateView.as_view(), name="create-category")]
