# DjangoUsers
Trying to get the most out of user django

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
