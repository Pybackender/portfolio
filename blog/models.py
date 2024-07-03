import uuid
from django.conf import settings
from django.db import models
from painless.models.mixins import OrganizedMixin

class Tag(OrganizedMixin):
    
    class Meta:
        ordering = [ '-published_at' ]
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
    
    def __str__(self):
        return self.title

class Post(OrganizedMixin):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = '+', on_delete = models.CASCADE)
    banner = models.ImageField(upload_to = 'blog/%Y/%m/%d', null = True, blank = True)
    tags = models.ManyToManyField(Tag, related_name = 'tags',  blank = True)
    content = models.TextField(blank=True,null=True)
    viewers = models.PositiveIntegerField(default=0)
    

    class Meta:
        ordering = ['-published_at', 'title']
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        get_latest_by = ['-published_at']
    
    def __str__(self):
        return self.title


 


   