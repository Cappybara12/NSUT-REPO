from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AsUser

# Register your models here.
@admin.register(AsUser)
class AsUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('phone',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','is_staff', 'is_active')}
         ),
    )
    list_filter = ['phone']
    list_display = [
        'id',
        'name',
        'phone',
        'level',
        'otp',
        'createdAt'
    ]
    ordering = ['phone']
    search_fields = ('phone',)
    filter_horizontal = ()
