from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from staff.serializers import TeamListSerializer, TeamDetailSerializer, EmployeeListSerializer, EmployeeDetailSerializer
from staff.models import Team, Employee
from user.permissions import IsManagementTeamMember


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class AllTeamViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = TeamListSerializer  # default serializer
    detail_serializer_class = TeamDetailSerializer

    permission_classes = [IsAuthenticated & IsManagementTeamMember]

    def get_queryset(self):
        return Team.objects.all()


class AllEmployeeViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = EmployeeListSerializer
    detail_serializer_class = EmployeeDetailSerializer

    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated & IsManagementTeamMember]

    def get_queryset(self):
        return Employee.objects.all()


    # def perform_create(self, serializer):
    #     team = Team.objects.get(id=self.kwargs['team_pk'])
    #     serializer.save(team=team)


class EmployeeViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = EmployeeListSerializer
    detail_serializer_class = EmployeeDetailSerializer

    permission_classes = [IsAuthenticated & IsManagementTeamMember]

    def get_queryset(self):
        return Employee.objects.filter(team_id=self.kwargs['team_pk'])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['team_id'] = self.kwargs['team_pk']
        return context
