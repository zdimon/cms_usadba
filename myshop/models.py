from shop.models import Product
from django.db import models

class Issue(Product):
    # The author should probably be a foreign key in the real world, but
    # this is just an example
    author = models.CharField(max_length=255)
    cover_picture = models.ImageField(upload_to='img/issue')
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['author']