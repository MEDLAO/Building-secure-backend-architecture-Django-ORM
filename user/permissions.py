from rest_framework import permissions
from rest_framework.permissions import BasePermission
from staff.models import Employee


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsManagementTeamMember(BasePermission):

    message = "You don't belong to Management Team"

    def has_permission(self, request, view):
        if request.method == 'POST' or view.action == 'list':
            management_team_employees = Employee.objects.filter(team__department='Management')
            return request.user.employee in management_team_employees
        return True

    def has_object_permission(self, request, view, obj):
        management_team_employees = Employee.objects.filter(team__department='Management')
        return request.user.employee in management_team_employees


class IsSalesTeamMember(BasePermission):

    message = "You don't belong to Sales Team"

    def has_permission(self, request, view):
        if request.method == 'POST' or view.action == 'list':
            sales_team_employees = Employee.objects.filter(team__department='Sales')
            return request.user.employee in sales_team_employees
        return True

    def has_object_permission(self, request, view, obj):
        sales_team_employees = Employee.objects.filter(team__department='Sales')

        if request.method == 'DELETE':
            return False
        else:
            return request.user.employee in sales_team_employees


class IsSupportTeamMember(BasePermission):

    message = "You don't belong to Support Team"

    def has_permission(self, request, view):
        if request.method == 'POST':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        support_team_employees = Employee.objects.filter(team__department='Support')

        if request.method == 'DELETE':
            return False
        else:
            return request.user.employee in support_team_employees
