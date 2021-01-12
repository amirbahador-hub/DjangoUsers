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