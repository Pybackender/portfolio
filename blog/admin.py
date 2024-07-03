from django.contrib import admin
from . models import Post, Tag
# admin.site.register(Post)
# admin.site.register(Tag)


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug',
                     'published_at', 'status', 'viewers', 'created', 'updated','is_published']
    list_filter = [ 'created', 'updated','tags']
    list_editable = ['viewers']


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug',
                     'published_at', 'status', 'created', 'updated']
    list_filter = [ 'created', 'updated']