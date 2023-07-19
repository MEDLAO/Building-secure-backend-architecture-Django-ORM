from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from user.managers import CustomUserManager


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.id) + " - " + str(self.email)


management_team, created_a = Group.objects.get_or_create(name='Management-Team')
sales_team, created_b = Group.objects.get_or_create(name='Sales-Team')
support_team, created_c = Group.objects.get_or_create(name='Support-Team')


def group_permissions(group, crud_operations, model_list):
    for model in model_list:
        for operation in crud_operations:
            permission = Permission.objects.get(name='Can' + " " + operation + " " + model)
            group.permissions.add(permission)


all_operations = ['add', 'change', 'delete', 'view']
change_and_view = ['change', 'view']
model_list_1 = ['user', 'employee']
model_list_2 = ['team', 'customer', 'contract', 'event']
group_permissions(management_team, all_operations, model_list_1)
group_permissions(management_team, change_and_view, model_list_2)


add_change_view = ['add', 'change', 'view']
model_list_3 = ['customer', 'contract', 'event']
group_permissions(sales_team, add_change_view, model_list_3)

model_list_4 = ['customer', 'event']
group_permissions(support_team, change_and_view, model_list_4)


# employee_in_management_team = [Employee.objects.filter(team__department='Management')]
# user_in_management_team = [employee.user for employee in employee_in_management_team]
#
# employee_in_sales_team = [Employee.objects.filter(team__department='Sales')]
# user_in_sales_team = [employee.user for employee in employee_in_sales_team]
#
# for user in User.objects.all():
#     if user in user_in_sales_team:
#         sales_team.user_set.add(user)
