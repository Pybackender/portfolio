from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import validate_email
from django.db import models
from django.templatetags.static import static
from painless.models.validations import validate_phone_number


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس IP')
    create = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ بازدید')

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name = 'ip'
        verbose_name_plural = 'ips'


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, validators=[validate_email])
    mobile = models.CharField(max_length=12, validators=[
                              validate_phone_number])
    address = models.CharField(max_length=225, blank=True, null=True)
    ################################################################
    avatar = models.ImageField(
        upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    instagram = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('../static/assets/img/profile-picture-1.jpg')
