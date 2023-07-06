from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from staff.models import Team, Employee


class TeamListSerializer(ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'department', 'manager', 'name', 'email_team', 'phone', 'employees']


class TeamDetailSerializer(ModelSerializer):

    employees = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'department', 'manager', 'name', 'email_team', 'phone', 'employees']

    def get_employees(self, instance):
        queryset = instance.employees.all()
        serializer = EmployeeListSerializer(queryset, many=True)
        return serializer.data


class EmployeeListSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'user', 'team']


class EmployeeDetailSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'user', 'status_employee', 'phone', 'team', 'is_staff', 'is_admin']
