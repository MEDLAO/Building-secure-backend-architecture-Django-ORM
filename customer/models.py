from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from staff.models import Employee


class Customer(models.Model):

    def __str__(self):
        return str(self.representative) + "-" + str(self.status_customer)

    class StatusCustomer(models.TextChoices):
        POTENTIAL = 'Potential'
        EXISTING = 'Existing'

    representative = models.CharField(max_length=50)
    email_customer = models.EmailField(unique=True)
    status_customer = models.CharField(choices=StatusCustomer.choices, max_length=9)
    phone = PhoneNumberField(null=False, blank=True, unique=True)
    company = models.CharField(max_length=30)


class Contract(models.Model):

    def __str__(self):
        return str(self.name) + "-" + str(self.signing_date)

    class StatusContract(models.TextChoices):
        OPEN = 'Open'
        CLOSED = 'Closed'

    status_contract = models.CharField(choices=StatusContract.choices, max_length=6)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2048)
    signing_date = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name='contracts')
    sales_employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name='contract_sales')
    support_employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name='contract_support')


class Event(models.Model):

    def __str__(self):
        return str(self.name) + "-" + str(self.start_date)

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2048, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, unique=True, related_name='event')
