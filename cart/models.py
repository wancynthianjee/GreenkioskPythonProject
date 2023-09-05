from django.db import models
from inventory.models  import Product
class Cart(models.Model):
    products=models.ManyToManyField(Product)
    customer_ID = models.IntegerField()
    list_of_items = models.IntegerField()
    quantity_of_items = models.CharField(max_length=6)

class Meta:
    verbose_name = 'Cart'
    verbose_name_plural = 'Carts'