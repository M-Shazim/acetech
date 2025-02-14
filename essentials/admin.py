from django.contrib import admin
from .models import Product, Cart

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    search_fields = ('title', 'category')
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
