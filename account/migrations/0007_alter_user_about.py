# Generated by Django 5.0.6 on 2024-07-27 07:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=ckeditor.fields.RichTextField(default=0),
            preserve_default=False,
        ),
    ]
