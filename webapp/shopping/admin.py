# shopping/admin.py

from django.contrib import admin
from .models import ShoppingList, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_purchased', 'shopping_list')
    search_fields = ('name',)
    list_filter = ('is_purchased',)

class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)

admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(Product, ProductAdmin)
