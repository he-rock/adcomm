from rest_framework import serializers
from core.models import File, Category


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ["user", "id"]


class CategorySerializer(serializers.ModelSerializer):
    image = FileSerializer()

    class Meta:
        model = Category
        fields = [
            "id",
            "user",
            "category",
            "name",
            "slug",
            "image",
        ]
        read_only_fields = [
            "id",
            "user",
            "slug",
        ]
