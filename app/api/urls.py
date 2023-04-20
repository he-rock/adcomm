from django.urls import path
from api.views import CategoryListView, CategoryRetrieveView, SubCategoryListView

app_name = "api"

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/<slug>/", CategoryRetrieveView.as_view(), name="category_detail"),
    path(
        "categories/<slug>/categories/",
        SubCategoryListView.as_view(),
        name="sub_category-list",
    ),
]
