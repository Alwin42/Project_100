import random
import string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_otp_email(email, otp):
    subject = f"{otp} is your Apex Rentals Login Code"
    
    # --- 1. The Professional HTML Design ---
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }}
            .container {{ width: 100%; padding: 40px 0; }}
            .card {{ background-color: #ffffff; width: 100%; max-width: 450px; margin: 0 auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); overflow: hidden; border: 1px solid #e0e0e0; }}
            .header {{ background-color: #061E29; padding: 20px; text-align: center; }}
            .header h1 {{ color: #5F9598; margin: 0; font-size: 24px; letter-spacing: 1px; text-transform: uppercase; }}
            .content {{ padding: 30px 20px; text-align: center; color: #333333; }}
            .otp-box {{ background-color: #f8f9fa; border: 2px dashed #5F9598; color: #061E29; font-size: 32px; font-weight: bold; letter-spacing: 5px; padding: 15px; margin: 20px 0; display: inline-block; border-radius: 6px; }}
            .footer {{ padding: 20px; text-align: center; font-size: 12px; color: #888888; background-color: #eeeeee; }}
            .warning {{ font-size: 13px; color: #666; margin-top: 20px; line-height: 1.5; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <div class="header">
                    <h1>Apex Rentals</h1>
                </div>
                
                <div class="content">
                    <p style="font-size: 16px; margin-bottom: 10px;">OTP</p>
                    <p>Use the verification code below to login to your account.</p>
                    
                    <div class="otp-box">{otp}</div>
                    
                    <p class="warning">
                        This code is valid for <strong>5 minutes</strong>.<br>
                        If you did not request this code, please ignore this email.
                    </p>
                </div>
                
                <div class="footer">
                    &copy; 2026 Apex Rentals. All rights reserved.<br>
                    Kochi, Kerala
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    # --- 2. Create the Plain Text Version (Fallback) ---
    text_content = strip_tags(html_content)

    # --- 3. Construct and Send the Email ---
    email_message = EmailMultiAlternatives(
        subject,
        text_content,        # Plain text version (for smart watches, old clients)
        settings.EMAIL_HOST_USER,
        [email]
    )
    email_message.attach_alternative(html_content, "text/html") # Attach the fancy HTML
    email_message.send()