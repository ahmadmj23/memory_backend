from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer, OTPVerifySerializer, UserSerializer
from .utils import send_otp_email
from .models import User
from django.utils import timezone
from datetime import timedelta
from drf_spectacular.utils import extend_schema

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = 'auth_login' # Reuse login throttle or define separate ones

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Send OTP
        send_otp_email(user)
        
        return Response({
            "message": "User created successfully. Please verify your email.",
            "email": user.email
        }, status=status.HTTP_201_CREATED)

class OTPVerifyView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OTPVerifySerializer
    throttle_scope = 'auth_otp'

    @extend_schema(request=OTPVerifySerializer, responses={200: "Success"})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
             # Return generic error to avoid enumeration
             return Response({"error": "Invalid details"}, status=status.HTTP_400_BAD_REQUEST)

        if str(user.otp_code) != str(otp):
             return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check expiry (10 mins)
        if user.otp_created_at < timezone.now() - timedelta(minutes=10):
             return Response({"error": "OTP Expired"}, status=status.HTTP_400_BAD_REQUEST)
        
        user.is_active = True
        user.is_verified = True
        user.otp_code = None # Clear OTP
        user.save()
        
        return Response({"message": "Account verified successfully. You can now login."}, status=status.HTTP_200_OK)

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # TODO: Implement token blacklisting here
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
