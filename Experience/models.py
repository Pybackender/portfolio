from django.db import models
from django.conf import settings
from painless.models.mixins import OrganizedMixin


class EXPERIENCE(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    DJANGO_ICONS = {
        "ICONS": {
            "edit": {"name": "fa-solid fa-pencil"},
        },
    }
    content = models.TextField(blank=True, null=True)
    datetime_year = models.IntegerField(null=False)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'EXPERIENCE'
        verbose_name = 'EXPERIENCES'
        get_latest_by = ['-published_at']

    def __str__(self):
        return self.title
