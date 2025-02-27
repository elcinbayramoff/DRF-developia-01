from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from .utils import generate_otp
from .models import OTP
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            user.is_active = False
            user.save()
            otp_code = generate_otp()
            email = validated_data.get('email')
            otp = OTP.objects.create(otp=otp_code, email=email)
            print(otp_code)
            Profile.objects.create(user=user)
            return user
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
class RegisterVerifySerializer(serializers.Serializer):
    otp = serializers.CharField()
    email = serializers.EmailField()