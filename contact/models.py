from django.db import models
from django.core.validators import validate_email
from painless.models.mixins import TimeStampedMixin


class Contact(TimeStampedMixin):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True,
                              validators=[validate_email])
    mobile_number = models.IntegerField()
    message = models.TextField()

    class Meta:
        ordering = ['-created']
        verbose_name = "contact"
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.name
