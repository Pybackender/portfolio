from django.db import models
from django.core.validators import validate_email
from painless.models.validations import validate_phone_number
from painless.models.mixins import TimeStampedMixin


class Contact(TimeStampedMixin):
    name = models.CharField(max_length=128)
    email = models.EmailField(
                              validators=[validate_email])
    mobile_number = models.CharField(max_length=15,blank=True,null=True,validators=[validate_phone_number])
    message = models.TextField()

    class Meta:
        ordering = ['-created']
        verbose_name = "contact"
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.name
