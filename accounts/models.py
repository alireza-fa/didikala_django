from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11, verbose_name=_('phone number'), unique=True)
    email = models.EmailField(max_length=120, verbose_name=_('email'), null=True, blank=True, unique=True)
    username = models.CharField(max_length=32, verbose_name=_('username'), unique=True)
    fullname = models.CharField(max_length=32, verbose_name=_('fullname'), null=True, blank=True)
    nationality_code = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('nationality code'))
    received_news = models.BooleanField(default=False, verbose_name=_('received news'))
    image = models.ImageField(verbose_name=_('image'), null=True, blank=True)
    city = models.CharField(max_length=32, verbose_name=_('city'), null=True, blank=True)
    is_oversea = models.BooleanField(default=False, verbose_name=_('is oversea'), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    is_admin = models.BooleanField(default=False, verbose_name=_('is admin'))
    score = models.PositiveIntegerField(verbose_name=_('score'), null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('email', )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin
