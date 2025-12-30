from rest_framework import serializers
from .models import *



class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["fullname", "email", "password", "phone", "create_at", "update_at"]
        
        
class SigninSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    
class ChangePasswordSerializers(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    
    
class CreateOtpSerializers(serializers.Serializer):
    email = serializers.CharField()
    
class RestPasswordSerializers(serializers.Serializer):
    email = serializers.CharField()
    new_password = serializers.CharField()
    otp = serializers.CharField()