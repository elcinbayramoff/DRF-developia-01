from .views import RefreshTokenView, RegisterView, LoginView, ProfileView, RegisterVerifyView
from django.urls import path
from django.conf import settings



urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view(), name='register'),
    path('register-verify/', RegisterVerifyView.as_view()),
    path('profile/', ProfileView.as_view(), name='profile'),
]

#Authorization: Bearer <token>