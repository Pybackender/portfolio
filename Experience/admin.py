from django.contrib import admin
from . models import EXPERIENCE


@admin.register(EXPERIENCE)
class EXPERIENCEadmin(admin.ModelAdmin):
    list_display = ['title', 'slug',
                    'datetime_year','DJANGO_ICONS']
    list_filter = ['datetime_year']
    prepopulated_fields = {'slug': ('title',)}
