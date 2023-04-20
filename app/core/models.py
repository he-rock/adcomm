from django.db import models
from django.contrib.auth import get_user_model


class File(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.ImageField(upload_to="%Y/%m/%d")
    blurhash = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "files"

    def __str__(self) -> str:
        return str(self.file.name)


class Category(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="parent_category",
    )
    image = models.ForeignKey(
        File,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return str(self.name)
