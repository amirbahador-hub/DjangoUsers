from datetime import timedelta
from djmoney.models.fields import MoneyField
from django.core.exceptions import ValidationError
from django.db import models
from .managers import ProductManager


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


class Store(models.Model):
    logo = models.ImageField(upload_to='store/', blank=True, null=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=512)
    activated = models.BooleanField(default=True)
    slug_url = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/ Y/% m/% d/', blank=True, null=True)
    spoiled_delta = models.DurationField(default=timedelta(days=15))

    stores = models.ManyToManyField(
        Store,
        through='ProductStore',
        through_fields=('product', 'store')
    )
    objects = ProductManager()

    def __str__(self) -> str:
        return f'{self.title} / {self.activated}'


class ProductStore(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='IRR'
    )

    def __str__(self) -> str:
        return f'{self.product.title} / {self.store.name}'


class Comment(models.Model):
    body = models.TextField()
    replied_to = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)


