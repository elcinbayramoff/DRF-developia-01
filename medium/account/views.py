from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .models import Profile, OTP
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProfileSerializer, RegisterVerifySerializer
from rest_framework.throttling import AnonRateThrottle
from rest_framework.validators import ValidationError
from rest_framework.response import Response


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

class RegisterVerifyView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        try:
            otp_instance = OTP.objects.get(email=email, otp=otp)
            user = User.objects.filter(email=email).first()
            user.is_active = True
            user.save()
            otp_instance.delete()
            return Response({'detail':'Account verified successfully'})
        except OTP.DoesNotExist:
            raise ValidationError({'detail':'Otp does not exist'})
        
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