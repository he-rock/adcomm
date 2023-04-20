import blurhash
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from core.models import Category, File


@receiver(pre_save, sender=Category)
def pre_save_category(sender, instance: Category, *args, **kwargs):
    if len(instance.slug) == 0:
        instance.slug = slugify(instance.name)


@receiver(post_save, sender=File)
def post_save_file(sender, instance: File, created: bool, *args, **kwargs):
    if created:
        with open(instance.file.path, "rb") as image_file:
            hash = blurhash.encode(image_file, x_components=4, y_components=3)
            instance.blurhash = str(hash)
            instance.save()
