from django.contrib import admin

# Register your models here.
from .models import Products

class AdminChanges(admin.ModelAdmin):
    readonly_fields = ('created_date','product_id')
    list_display = ('product_name', 'selling_price', 'cost_price','stock','created_date','product_id')

admin.site.register(Products, AdminChanges)