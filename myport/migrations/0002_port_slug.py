# Generated by Django 5.0.6 on 2024-07-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
