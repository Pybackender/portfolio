# Generated by Django 5.0.6 on 2024-08-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.CharField(max_length=500),
        ),
    ]
