from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from user.managers import CustomUserManager

from staff.models import Employee


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return str(self.id) + " - " + str(self.email)

    # managers = Group.objects.get_or_create(name='managers')
    # sales = Group.objects.get_or_create(name='sales')
    # support = Group.objects.get_or_create(name='support')


    # managers.permissions.set([permission_list])

    # def save(self, *args, **kwargs):
    #     managers = Group.objects.get(name="managers")
    #     self.groups.add(managers)
    #     super().save(*args, **kwargs)
