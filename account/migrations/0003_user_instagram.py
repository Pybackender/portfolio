# Generated by Django 5.0.6 on 2024-07-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_ipaddress_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
    ]
