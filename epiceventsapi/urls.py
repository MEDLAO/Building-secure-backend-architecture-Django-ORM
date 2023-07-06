"""epiceventsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from staff.views import AllTeamViewset, AllEmployeeViewset, EmployeeViewset
from customer.views import AllCustomerViewset, AllContractViewset, AllEventViewset, ContractViewset, EventViewset


first_router = routers.SimpleRouter()
first_router.register('all-teams', AllTeamViewset, basename='team')
first_router.register('all-employees', AllEmployeeViewset, basename='employee')
first_router.register('all-customers', AllCustomerViewset, basename='customer')
first_router.register('all-contracts', AllContractViewset, basename='contract')
first_router.register('all-events', AllEventViewset, basename='event')

second_router = routers.SimpleRouter()
second_router.register('employees', EmployeeViewset, basename='team-employee')
second_router.register('events', EventViewset, basename='contract-event')
second_router.register('contracts', ContractViewset, basename='customer-contract')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('user.urls')),
    path('api/', include(first_router.urls)),
    path('api/all-teams/<int:team_pk>/', include(second_router.urls)),
    path('api/all-contracts/<int:contract_pk>/', include(second_router.urls)),
    path('api/all-customers/<int:customer_pk>/', include(second_router.urls)),
]
