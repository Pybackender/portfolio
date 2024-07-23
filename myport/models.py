from django.db import models


class Port(models.Model):
    slug = models.SlugField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    

class Meta:
    ordering = ['-published_at']
    verbose_name = 'portfolio'
    verbose_name_plural = 'portfolios'
    

def __str__(self):
        return self.image
