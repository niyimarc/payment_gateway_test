# admin.py
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'delivered_date', 'created_on', 'updated_on')
    list_filter = ('payment_method', 'delivered_date', 'payment_date')
    readonly_fields = ('payment_made', 'order_placed', 'payment_date', 'status', 'order_reference', 'user')
    search_fields = ('user__username', 'total_price')

# Register the Order model with the custom admin class
admin.site.register(Order, OrderAdmin)
