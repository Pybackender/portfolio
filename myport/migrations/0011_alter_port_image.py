# Generated by Django 5.0.6 on 2024-08-09 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myport', '0010_alter_category_options_rename_name_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d'),
        ),
    ]
