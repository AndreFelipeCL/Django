from django.contrib import admin

# Register your models here.
from catalog.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'created', 'updated']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
