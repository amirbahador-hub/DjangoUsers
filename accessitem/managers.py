from django.db import models
from django.db.models import Count, Min, Max, F


class ProductQuerySet(models.QuerySet):
    def business_layer(self):
        return self.filter(activated=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def business_layer(self):
        return self.get_queryset().business_layer()



