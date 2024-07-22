from django.contrib import admin
from .models import User, IPAddress
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .actions import make_active, make_deactive

admin.site.register(IPAddress)
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('mobile','username', 'first_name', 'last_name', 'address','title','about','linkedin','whatsapp','instagram')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email','username', 'first_name', 'last_name', 'is_active')
    search_fields = ('email', 'mobile', 'last_name')

    
    actions = [make_active, make_deactive]
    ordering = ('email',)


