# Generated by Django 5.0.6 on 2024-08-06 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myport', '0009_category_port_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
    ]
