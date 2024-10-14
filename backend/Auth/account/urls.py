from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    # path('delete_account/', DeleteUser.as_view(), name='delete'),
]
