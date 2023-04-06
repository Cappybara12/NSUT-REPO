from django.contrib import admin
from .models import MultiToken

# Register your models here.


@admin.register(MultiToken)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['id','user','key']