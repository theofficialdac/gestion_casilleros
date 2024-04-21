from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rut', 'telefono')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('rut', 'telefono')}),
    )
    list_display = ['email', 'nombre', 'apellido', 'rut', 'telefono', 'is_staff', 'is_active']
    search_fields = ['email', 'nombre', 'apellido', 'rut', 'telefono']
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
