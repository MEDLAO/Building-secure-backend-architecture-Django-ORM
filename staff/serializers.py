from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from staff.models import Team, Employee


class TeamListSerializer(ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'department', 'name', 'email_team', 'phone', 'employees']


class TeamDetailSerializer(ModelSerializer):

    employees = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'department', 'name', 'email_team', 'phone', 'employees']

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

    def validate_team(self, value):
        team = Team.objects.get(id=self.context['team_id'])
        if value == team:
            return value
        raise serializers.ValidationError('Wrong team !')

    def validate_status_employee(self, value):
        team = Team.objects.get(id=self.context['team_id'])
        if value == "Manager" and team.employees.filter(status_employee=value).exists():
            raise serializers.ValidationError('There is already a Manager for this team')
        elif value == "Employee" and not team.employees.filter(status_employee='Manager').exists():
            raise serializers.ValidationError('The first member must be a Manager')
        return value
