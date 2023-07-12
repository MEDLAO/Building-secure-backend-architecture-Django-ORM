from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Team(models.Model):

    def __str__(self):
        return self.name + "-" + self.department

    class Department(models.TextChoices):
        MANAGEMENT = 'Management'
        SALES = 'Sales'
        SUPPORT = 'Support'

    department = models.CharField(choices=Department.choices, max_length=10)
    name = models.CharField(max_length=50, blank=True)
    email_team = models.EmailField(unique=True)
    phone = PhoneNumberField(null=False, blank=True, unique=True)

    # class Meta:
    #     db_table = 'Team'
    #     unique_together = (('manager', 'department'),)  # for composite primary key


class Employee(models.Model):

    def __str__(self):
        return str(self.user) + "-" + str(self.team)

    class StatusEmployee(models.TextChoices):
        EMPLOYEE = 'Employee'
        MANAGER = 'Manager'

    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee')
    status_employee = models.CharField(choices=StatusEmployee.choices, max_length=8)
    phone = PhoneNumberField(null=False, blank=True, unique=True)
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name='employees')
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

