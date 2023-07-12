from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User
from customer.models import Customer, Contract, Event
from staff.models import Team, Employee
from user.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("id", "email", "is_staff", "is_active", "first_name", "last_name")
    list_filter = ("id", "email", "is_staff", "is_active", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "first_name", "last_name", "is_staff",
                "is_active", "groups", "user_permissions"
            )}),
    )
    search_fields = ("email",)
    ordering = ("email",)


class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'email')


class TeamAdmin(admin.ModelAdmin):

    list_display = ('id', 'department', 'name', 'email_team', 'phone',)


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'status_employee', 'phone', 'team',)


class CustomerAdmin(admin.ModelAdmin):

    list_display = ('id', 'representative', 'email_customer', 'status_customer', 'phone', 'company',)


class ContractAdmin(admin.ModelAdmin):

    list_display = ('id', 'status_contract', 'name', 'description', 'signing_date', 'customer', 'sales_employee', 'support_employee',)


class EventAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'start_date', 'end_date', 'contract',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
