from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.authentication import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import random
from .utils import *



@api_view(['POST'])
def signup(request):
    serializers = UserCreateSerializers(data=request.data)
    serializers.is_valid(raise_exception=True)
    
    password=serializers.validated_data['password']
    user = CustomUser(
        fullname=serializers.validated_data['fullname'],
        email=serializers.validated_data['email'],
        phone=serializers.validated_data['phone']
    )
    
    user.set_password(password)
    user.save()
    return Response({"message": "user registration successful!"}, status=status.HTTP_200_OK)



@api_view(["POST"])
def signin(request):
    serializers = SigninSerializers(data=request.data)
    if not serializers.is_valid():
        return Response({"message": "Please provide valid information."}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(
        request,
        email=serializers.validated_data["email"],
        password=serializers.validated_data["password"]
    )
    
    if user is not None:
        token = get_tokens_for_user(user)
        return Response(
            {
                "message": "Login successful",
                "access_token" : token["access"],
                "refresh_token": token["refresh"]
            }, 
            status=status.HTTP_200_OK)
    return Response({"message": "In valid email or password"},status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def change_password(request):
    serializers = ChangePasswordSerializers(data=request.data)
    serializers.is_valid(raise_exception=True)
    
    user = get_object_or_404(CustomUser, id=request.user.id)
    if user.check_password(serializers.validated_data["old_password"]):
        user.set_password(serializers.validated_data["new_password"])
        user.save()
        return Response({"message": "password change successful"}, status=status.HTTP_200_OK)
    return Response({"message": "In valid old password"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def send_otp(request):
    serializers = CreateOtpSerializers(data=request.data)
    serializers.is_valid(raise_exception=True)
    
    email=serializers.validated_data['email']
    
    if CustomUser.objects.filter(email=email).exists():
        user = CustomUser.objects.get(email=email)
        
        otp = {
            "user": user,
            'otp' : random.randint(10000, 99999)
        }
        
        OTP.objects.create(**otp)
        return Response({
            "status" : "success",
            "message": "otp create success."
        }, status=status.HTTP_200_OK)
    
    return Response({
        "status": "failed",
        "message": "wrong email dosenot exists."
        
    }, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["POST"])
@permission_classes([AllowAny])
def reset_password(request):
    serializers = RestPasswordSerializers(data=request.data)
    serializers.is_valid(raise_exception=True)
    
    email = serializers.validated_data["email"]
    otp = serializers.validated_data["otp"]
    new_password = serializers.validated_data["new_password"]
    
    if CustomUser.objects.filter(email=email).exists():
        user = CustomUser.objects.get(email__iexact=email)
        db_otp = OTP.objects.filter(user=user).last()
        
        if str(otp) == str(db_otp.otp):
            if not db_otp.is_expired():
                return Response({
                    "status" : "error",
                    "message": "Otp time expired"
                }, status=status.HTTP_400_BAD_REQUEST)
                
            user.set_password(new_password)
            user.save()
            
            return Response({
                "status": "success",
                "message": "Password Reset Successfully."
            }, status=status.HTTP_200_OK)
    
        return Response({
            "status": "failed",
            "message": "Wrong otp."
        }, status=status.HTTP_400_BAD_REQUEST)
        
    return Response({
        "status": "failed",
        "message": "email dosenot exists."
    }, status=status.HTTP_400_BAD_REQUEST)