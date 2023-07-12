from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import RegisterView


urlpatterns = [
    path('api/signup/', RegisterView.as_view(), name="sign_up"),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
