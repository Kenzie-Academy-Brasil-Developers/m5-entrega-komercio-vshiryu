from django.db import models
from uuid import uuid4

from traitlets import default

# Create your models here.


class Product(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    seller = models.ForeignKey(
        "user.Account", on_delete=models.CASCADE, related_name="products", null=True
    )
