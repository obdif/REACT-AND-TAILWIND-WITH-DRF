# import random
# from django.core.mail import EmailMessage
# from django.conf import settings
# from .models import *


# def generateOtp():
#     otp=""
#     for i in range(6):
#         otp +=str(random.randint(0,9))
#     return otp


    
    
    
# def send_code(email):
#     Subject="ONE TIME PASSCODE FOR EMAIL VERIFICATION"
#     otp_code = generateOtp()
#     print(otp_code)
#     user=User.objects.get(email=email)
#     current_site="https://react-tailwind-roan.vercel.app/"
#     email_body=f"Hi {user.email} \n Thanks for signing up on {current_site} please verify your email with the one time passcode \n {otp_code}"
#     from_email = settings.DEFAULT_FROM_EMAIL
    
#     OneTimePassword.objects.create(user=user, code=otp_code)
    
#     send_email=EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])
    
#     send_email.send(fail_silently=True)
    
    
# # def send_normal_email(data):
# #     email=EmailMessage(
# #         subject=data['email_subject'],
# #         body=data['email_body'],
# #         from_email=settings.EMAIL_HOST_USER,
# #         to=[data['to_email']]
# #     )
# #     email.send()