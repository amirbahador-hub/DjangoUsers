# DjangoUsers
Trying to get the most out of user django


# Table of Content
1. [Customize User](#customize-user)
2. [Select Related](#use-related-name)
3. [Setting](#modular-django)


___

#### Bpython
i really love bpython 
```bash
pip install bpython
```
#### use related name
parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
```python
from accessitem.models import *

book = Category.objects.get(title='books')
Category.objects.create(title='self help book', parent=book)
Category.objects.create(title='programming book', parent=book)
book.children.all()

```
they all do the same thing
```python
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=512)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)

book = Category.objects.get(title='books')
# first method
book.children.all()
# second method
Category.objects.select_related('parent').all()
# third method
Category.objects.prefetch_related('parent').all()
```

#### modular Django
```bash
export DJANGO_SETTINGS_MODULE=mysites.settings
```
you should add another parent
```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
```
check base dir with bpython in terminal
```python
from DjangoUsers.settings import base
base.BASE_DIR
```

### User

#### customize user

https://dev.to/joshwizzy/customizing-django-authentication-using-abstractbaseuser-llg
##### in settings
```python
INSTALLED_APPS = []
INSTALLED_APPS +=  'usersgeteway'
AUTH_USER_MODEL = 'usersgeteway.BaseUser'
```
##### in models
```python
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager as BUM,
    PermissionsMixin,
    AbstractBaseUser
)
from django.contrib.auth import get_user_model
from common.models import BaseModel


# Taken from here:
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
# With some modifications


class BaseUserManager(BUM):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin
```
##### in call
```python
"""instead of this"""
# from django.contrib.auth.models import User
"""DO this"""
from django.contrib.auth import get_user_model
User = get_user_model()
```
