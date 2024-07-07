from django.contrib import admin
from . models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created','mobile_number']
    list_filter = ['created']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


