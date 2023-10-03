from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'short_description', 'price', 'date_and_time')
    ordering = ('id',)

admin.site.register(Product, ProductAdmin)