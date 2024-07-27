# Generated by Django 5.0.6 on 2024-07-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Address',
            field=models.CharField(default=0, max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='fax',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
