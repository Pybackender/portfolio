from django.contrib import admin
from .models import  Category, Port

@admin.register(Port)
class Portadmin(admin.ModelAdmin):
    list_display = [ 'name','category','image',]
    prepopulated_fields = {'name': ('image',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title" , "slug"]
    prepopulated_fields = {'slug': ('title',)}