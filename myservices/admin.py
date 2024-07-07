from django.contrib import admin
from .models import service

@admin.register(service)
class serviceadmin(admin.ModelAdmin):
    list_display = ['title', 'slug',
                    'DJANGO_ICONS']
    prepopulated_fields = {'slug': ('title',)}