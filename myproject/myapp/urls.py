from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserLogoutView



urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='user-registration'),
    path('auth/login/', UserLoginView.as_view(), name='user-login'),
    path('auth/logout/', UserLogoutView.as_view(), name='user-logout'),
]