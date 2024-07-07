# Generated by Django 5.0.6 on 2024-07-07 12:35

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(help_text='The text must be unique', max_length=128, unique_for_month='published_at')),
                ('slug', models.CharField(max_length=128, unique_for_month='published_at')),
                ('status', models.IntegerField(choices=[(1, 'Send'), (2, 'Cancel')], default=2)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(help_text='The text must be unique', max_length=128, unique_for_month='published_at')),
                ('slug', models.CharField(max_length=128, unique_for_month='published_at')),
                ('status', models.IntegerField(choices=[(1, 'Send'), (2, 'Cancel')], default=2)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d')),
                ('content', models.TextField(blank=True, null=True)),
                ('viewers', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='blog.tag')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-published_at', 'title'],
                'get_latest_by': ['-published_at'],
            },
        ),
    ]
