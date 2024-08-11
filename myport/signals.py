import os
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Port


@receiver(models.signals.port_delete, sender=Port)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Port)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Port.objects.get(pk=instance.pk).image
    except Port.DoesNotExist:
        return False
    if not old_file:
        return
    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
