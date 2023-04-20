from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CategorySerializer
from core.models import Category


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "slug"


class SubCategoryListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        category = Category.objects.filter(slug=slug).first()
        return None if not category else Category.objects.filter(category=category)
