from django.db import models
from django.utils import timezone


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class OrganizedMixin(TimeStampedMixin):
    class Status(models.IntegerChoices):
        SEND = 1, 'Send'
        CANCELLED = 2, 'Cancel'
    title = models.CharField(
        max_length=128, unique_for_month='published_at', help_text="The text must be unique")
    slug = models.CharField(max_length=128, unique_for_month='published_at',)
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.CANCELLED
    )

    class Meta:
        abstract = True

    # def is_published(self):
    #     return self.status
    # is_published.boolean = True
