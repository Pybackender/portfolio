# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ExperienceExperience(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    icon = models.CharField(max_length=128, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    datetime_year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Experience_experience'


class AccountIpaddress(models.Model):
    ip_address = models.CharField(max_length=39)
    create = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'account_ipaddress'


class AccountUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    email = models.CharField(unique=True, max_length=254)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=225, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    whatsapp = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'account_user'


class AccountUserGroups(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_groups'
        unique_together = (('user', 'group'),)


class AccountUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class BlogPost(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    published_at = models.DateTimeField()
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    status = models.IntegerField()
    uid = models.CharField(primary_key=True, max_length=32)
    banner = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    viewers = models.PositiveIntegerField()
    author = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post'


class BlogPostTags(models.Model):
    post = models.ForeignKey(BlogPost, models.DO_NOTHING)
    tag = models.ForeignKey('BlogTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post_tags'
        unique_together = (('post', 'tag'),)


class BlogTag(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    published_at = models.DateTimeField()
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blog_tag'


class ContactContact(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    published_at = models.DateTimeField()
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=254)
    mobile_number = models.IntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'contact_contact'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MyservicesService(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    contact = models.TextField()
    icon = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'myservices_service'
