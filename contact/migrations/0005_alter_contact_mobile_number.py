# Generated by Django 5.0.6 on 2024-08-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_contact_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
