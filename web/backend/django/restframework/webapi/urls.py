from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path('hello', views.Hello.as_view(), name='hello'),
    path('hello2', views.HelloWithAuth.as_view(), name='hello2'),
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
