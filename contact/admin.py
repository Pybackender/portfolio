from django.contrib import admin
from . models import Contact
from painless.models.actions import ExportMixin, PostableMixin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin,PostableMixin,ExportMixin):
    list_display = ['name', 'email', 'created', 'mobile_number']
    list_filter = ['created']
    search_fields = ['name']

    actions = ['make_published', 'make_draft',
               'export_as_json', 'export_as_csv']
