from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken


# adeblessin4u@gmail.com 1234567890


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True, verbose_name=_("Email Address"))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Specify on_delete=models.CASCADE to handle deletion
    # groups = models.ManyToManyField(Group, related_name='account_user_groups', blank=True)
    # user_permissions = models.ManyToManyField(Permission, related_name='account_user_permissions', blank=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    

    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh':str(refresh),
    #         'access':str(refresh.access_token)
    #     }
        
        
# class OneTimePassword(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     otp = models.CharField(max_length=6, unique=True, blank=False, verbose_name=_("OTP"))
    
#     def __str__(self):
#         return f"{self.user.email}"