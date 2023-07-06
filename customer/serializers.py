from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from customer.models import Customer, Contract, Event

"""ListSerializer et DetailSerializer pour les trois classes"""


class CustomerListSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'representative', 'email_customer', 'status_customer', 'contracts']


class CustomerDetailSerializer(ModelSerializer):

    contracts = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'representative', 'email_customer', 'status_customer', 'phone', 'company', 'contracts']

    def get_contracts(self, instance):
        queryset = instance.contracts.all()
        serializer = ContractListSerializer(queryset, many=True)
        return serializer.data


class ContractListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'name', 'signing_date', 'event']


class ContractDetailSerializer(ModelSerializer):

    event = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['id', 'name', 'signing_date', 'customer', 'description', 'sales_employee', 'support_employee', 'event']

    def get_event(self, instance):
        queryset = instance.event.all()
        serializer = EventListSerializer(queryset, many=True)
        return serializer.data


class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'start_date', 'end_date']


class EventDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'contract']
