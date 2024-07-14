from django.contrib import admin
from . models import Post, Tag
from django.utils.html import format_html

from painless.models.actions import ExportMixin, PostableMixin



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug',
                     'published_at', 'status', 'created', 'updated']
    list_filter = [ 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin,PostableMixin, ExportMixin):
    list_display = ('thumbnail','title',
                     'published_at', 'status', 'viewers', 'created', 'updated','is_published')
    def thumbnail(self, object):
        if object.banner:
            return format_html('<img src="{}" width="40" style="border-radius:50%;">'.format(object.banner.url))
    list_filter = ('status', 'updated')
    list_display_links = ['title','thumbnail']
    search_fields = ('title', 'content')
    list_editable = ['viewers']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('title',), 
                    ('author', 'status', ),
                    ( 'viewers'),
                ),
            }                    
        ),

        ('Advanced_options', { 
            'fields': (
                    'tags',
                    'banner',
                    'content',
                    'published_at',
                ),
            'classes': ('collapse',)
            },

        ),
    ]

    def published(self, obj):
        return obj.published_at


    def is_published(self, obj):
        published = 1
        return obj.status == published
    is_published.boolean = True
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []


admin.site.site_header = "hsn"
admin.site.site_title = "حسن سایت ادمین"
admin.site.index_title = "خوش امدی حسن "