from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('orderitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    readonly_fields = (
        'order_number', 'date', 'order_total', 'stripe_pid'
    )

    fields = (
        'order_number', 'user_profile', 'date', 'full_name',
        'email', 'phone_number', 'country',
        'postcode', 'city', 'address_line1',
        'address_line2', 'order_total', 'stripe_pid'
    )

    list_display = (
        'order_number', 'date', 'full_name',
        'order_total'
    )

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)