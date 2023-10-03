from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    long_description = models.TextField(default="Add a long description about this product the usage, specs and more.")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    date_and_time = models.DateTimeField(auto_now_add=True)