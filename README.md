# DjangoUsers
Trying to get the most out of user django

#### use related name
parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
```python
from accessitem.models import *

book = Category.objects.get(title='books')
Category.objects.create(title='self help book', parent=book)
Category.objects.create(title='programming book', parent=book)
book.children.all()

```
