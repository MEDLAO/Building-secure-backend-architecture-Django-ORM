from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from customer.models import Customer, Contract, Event

from customer.serializers import CustomerListSerializer, CustomerDetailSerializer, ContractListSerializer, \
    ContractDetailSerializer, EventListSerializer, EventDetailSerializer

from user.permissions import IsSalesTeamMember, IsManagementTeamMember, IsSupportTeamMember


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class AllCustomerViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = CustomerListSerializer
    detail_serializer_class = CustomerDetailSerializer

    permission_classes = [IsAuthenticated & (IsSalesTeamMember | IsManagementTeamMember | IsSupportTeamMember)]

    def get_queryset(self):
        return Customer.objects.all()


class AllContractViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer

    permission_classes = [IsAuthenticated & (IsSalesTeamMember | IsManagementTeamMember)]

    def get_queryset(self):
        return Contract.objects.all()


class ContractViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer

    permission_classes = [IsAuthenticated & (IsSalesTeamMember | IsManagementTeamMember)]

    def get_queryset(self):
        return Contract.objects.filter(customer_id=self.kwargs['customer_pk'])


class AllEventViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer

    permission_classes = [IsAuthenticated & (IsSalesTeamMember | IsManagementTeamMember | IsSupportTeamMember)]

    def get_queryset(self):
        return Event.objects.all()


class EventViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer

    permission_classes = [IsAuthenticated & (IsSalesTeamMember | IsManagementTeamMember | IsSupportTeamMember)]

    def get_queryset(self):
        return Event.objects.filter(contract_id=self.kwargs['contract_pk'])
