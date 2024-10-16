# rentals/admin.py
from django.contrib import admin
from .models import Equipment, Booking

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_per_day')
    search_fields = ('name', 'category')

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Booking)
