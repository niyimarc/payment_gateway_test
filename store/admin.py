# admin.py
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'delivered_date', 'created_on', 'updated_on')
    list_filter = ('delivered_date', 'created_on', 'updated_on')
    search_fields = ('user__username', 'total_price')

# Register the Order model with the custom admin class
admin.site.register(Order, OrderAdmin)
