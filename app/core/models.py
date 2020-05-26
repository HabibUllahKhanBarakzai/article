from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Permission,
    PermissionsMixin,
)
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Q, Value
from django.utils import timezone

from . import UserTypes


class BaseTypeManager(models.Manager):

    """Custom QuerySet for writer model"""

    def create_type(self, user):
        """Creating a writer object"""
        user_type = self.model(
            user=user
        )
        user_type.save()
        return user_type


class UserManager(BaseUserManager):
    def create_user(
        self, email, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)

        extra_fields.pop("username", None)

        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )

    def staff(self):
        return self.get_queryset().filter(is_staff=True)


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=settings.DEFAULT_MAX_CHAR_LENGTH, blank=True)
    last_name = models.CharField(max_length=settings.DEFAULT_MAX_CHAR_LENGTH, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    type = models.CharField(max_length=settings.DEFAULT_MAX_CHAR_LENGTH,
                            choices=UserTypes.CUSTOM_TYPES,
                            default=UserTypes.ADMIN)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """get users full name"""
        if self.first_name or self.last_name:
            return ("%s %s" % (self.first_name, self.last_name)).strip()
        return self.email

    @property
    def is_writer(self):
        """ Check if the user is writer or not"""
        return True if self.writer else False

    @property
    def is_editor(self):
        """ Check if the user is writer or not"""
        return True if self.editor else False


class WriterManager(BaseTypeManager):
    """Writer Manager Can add more functionality in future"""
    pass


class Writer(models.Model):
    """model for writer"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="writer")

    objects = WriterManager()


class EditorManager(BaseTypeManager):
    """Editor Manager Can add more functionality in future"""
    pass


class Editor(models.Model):
    """model for editor"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="editor")

    objects = EditorManager()