from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

"""
TubularInline subclass defines the template used
to render the Order in the admin interface. StackInline is other one.
"""


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline,)


admin.site.register(Order, OrderAdmin)
