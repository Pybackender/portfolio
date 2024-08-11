from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ['title']
    indexes = [
        models.Index(fields=['title']),
    ]
    verbose_name = 'category'
    verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Port(models.Model):
    name = models.SlugField(max_length=50)
    image = models.ImageField(null=True, blank=True,upload_to='myport/%Y/%m/%d')
    link = models.CharField(max_length=225, null=True, blank=True)
    content = models.CharField(max_length=225, null=True, blank=True)
    category = models.ForeignKey(Category,
                                 related_name='Ports',
                                 on_delete=models.CASCADE)


class Meta:
    ordering = ['-published_at']
    verbose_name = 'portfolio'
    verbose_name_plural = 'portfolios'


def __str__(self):
    return self.image
