# Generated by Django 5.0.6 on 2024-08-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_contact_address_remove_contact_fax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
