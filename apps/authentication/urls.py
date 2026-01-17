from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView, OTPVerifyView, UserDetailView, LogoutView, ReviewerCreateView

urlpatterns = [
    path('reviewer/create', ReviewerCreateView.as_view(), name='reviewer-create'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('verify-otp', OTPVerifyView.as_view(), name='verify-otp'),
    path('user', UserDetailView.as_view(), name='user-detail'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
