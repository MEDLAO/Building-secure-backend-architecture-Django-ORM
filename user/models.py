from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from user.managers import CustomUserManager


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return str(self.id) + " - " + str(self.email)

    def save(self, *args, **kwargs):
        managers = Group.objects.get(name="managers")
        self.groups.add(managers)
        super().save(*args, **kwargs)
