from django.contrib.auth.models import BaseUserManager
import random


class UserManager(BaseUserManager):
    def create_user(self, phone_number, username=None, email=None, password=None):
        if not phone_number:
            raise ValueError('User must have phone number')
        if not username:
            username = str(random.randint(1111111, 99999999999))
        if not password:
            password = str(random.randint(10000000, 99999999))
        user = self.model(phone_number=phone_number, username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username=None, email=None, password=None, **extra_fields):
        user = self.create_user(phone_number, username, email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_or_create(self, phone_number):
        user = self.model.objects.filter(phone_number=phone_number)
        if user.exists():
            return user[0]
        return self.create_user(phone_number)
