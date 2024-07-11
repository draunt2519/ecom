from django.contrib import admin
from orderapp.models import Order
from orderapp.models import OrderDetail

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderDetailInline,
    ]
    list_display=["fullname","address","phone","total","created"]
    list_per_page = 10
    list_filter=["total"]
    search_fields=["fullname","address","phone"]

class OrderDetailAdmin(admin.ModelAdmin):
    list_display=["product","price","quantity","created","order"]
    list_per_page = 10
    list_filter=["product"]
    search_fields=["product","created","order"]

# Register your models here.
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)
