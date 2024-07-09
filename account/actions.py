
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


def make_deactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


make_active.short_description = ('activate')
make_deactive.short_description = ('deactivate')
