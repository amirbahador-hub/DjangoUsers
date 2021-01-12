from django.core.exceptions import ValidationError
from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=512)

    def clean(self):
        if self.title.isdigit():
            raise ValidationError("title must be meaningful not only digits")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=512)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)

    @property
    def get_children(self) -> object:
        return self.children.all()

    @property
    def get_children_select_related(self) -> object:
        return Category.objects.select_related('parent').all()

    @property
    def get_children_prefetch(self) -> object:
        return Category.objects.prefetch_related('parent').all()

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=512)




