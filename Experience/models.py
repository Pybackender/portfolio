from django.db import models
from django.conf import settings
from painless.models.mixins import OrganizedMixin


class EXPERIENCE(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    icon = models.CharField(max_length=128, blank = True, null = True)
    
    content = models.TextField(max_length=500,blank=True, null=True)
    datetime_year = models.IntegerField(null=False)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'EXPERIENCE'
        verbose_name = 'EXPERIENCES'
        get_latest_by = ['-published_at']

    def __str__(self):
        return self.title
