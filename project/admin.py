from django.contrib import admin
from .models import Category, Product, Review


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category']
    list_display = ['id', 'title', 'price', 'category']
    list_editable = ['price', 'title', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
