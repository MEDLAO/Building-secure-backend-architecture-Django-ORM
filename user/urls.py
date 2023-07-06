from django.urls import path
from user.views import RegisterView


urlpatterns = [
    path('api/signup/', RegisterView.as_view(), name="sign_up"),
]
