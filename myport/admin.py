from django.contrib import admin
from .models import Port

@admin.register(Port)
class Portadmin(admin.ModelAdmin):
    list_display = ['image', 'slug']
    prepopulated_fields = {'slug': ('image',)}
    
