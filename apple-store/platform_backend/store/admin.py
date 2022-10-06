from django.contrib import admin

from .models import products


@admin.register(products.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "upload",
        "default",
    ]
