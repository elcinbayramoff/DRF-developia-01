from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .models import Profile
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProfileSerializer
"""
IsAuthenticated - Tokeni var
AllowAny
IsAdminUser - Tokeni var
IsAuthenticatedOrReadOnly
"""
#Logout
#Login

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    
    
class LoginView(TokenObtainPairView):
    pass

class RefreshTokenView(TokenRefreshView):
    pass


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        print(self.request.user)
        return self.request.user.profile