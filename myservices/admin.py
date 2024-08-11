from django.contrib import admin
from .models import service

@admin.register(service)
class serviceadmin(admin.ModelAdmin):
    list_display = ['title', 'slug','contact','icon']
    prepopulated_fields = {'slug': ('title',)}