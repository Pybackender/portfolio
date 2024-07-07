from django.db import models


class service(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    contact = models.TextField(max_length=225)
    DJANGO_ICONS = {
        "ICONS": {
            "edit": {"name": "fa-solid fa-pencil"},
        },
    }

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'service'
        verbose_name = 'services'
        get_latest_by = ['-published_at']

    def __str__(self):
        return self.title
