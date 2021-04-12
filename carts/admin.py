from django.contrib import admin
from .models import Cart, Cartitem

# Register your models here.

class CartitemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'is_active')

admin.site.register(Cart)
admin.site.register(Cartitem, CartitemAdmin)
