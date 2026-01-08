import random
import string
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def send_otp_email(user):
    otp = generate_otp()
    user.otp_code = otp
    user.otp_created_at = timezone.now()
    user.save()

    subject = 'Your Verification Code'
    message = f'Hi {user.username},\n\nYour verification code is: {otp}\n\nThis code expires in 10 minutes.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    try:
        if settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD:
             send_mail(subject, message, from_email, recipient_list)
        else:
             print(f"DEV MODE: OTP for {user.email} is {otp}")
    except Exception as e:
        print(f"Error sending email: {e}")
