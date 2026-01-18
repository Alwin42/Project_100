import random
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    # Returns a random 6-digit string like "123456"
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    subject = 'Apex Rentals Login Code'
    message = f'Your secure login code is: {otp}. It expires in 5 minutes.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(subject, message, email_from, recipient_list)