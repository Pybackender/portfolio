# Generated by Django 5.0.6 on 2024-07-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Experience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='content',
            field=models.TextField(blank=True, max_length=225, null=True),
        ),
    ]
