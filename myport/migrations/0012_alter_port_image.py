# Generated by Django 5.0.6 on 2024-08-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myport', '0011_alter_port_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='myport/%Y/%m/%d'),
        ),
    ]