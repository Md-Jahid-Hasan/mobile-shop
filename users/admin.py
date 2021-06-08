from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Address, Person, Machine

admin.site.register(Address)
admin.site.register(Person)
admin.site.register(Machine)
# class AddressInline(GenericTabularInline):
#     model = Address
#
#
# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     inlines = [AddressInline, ]
#
#
# admin.site.register(Address)
#
#
# @admin.register(Machine)
# class MachineAdmin(admin.ModelAdmin):
#     inlines = [AddressInline, ]
