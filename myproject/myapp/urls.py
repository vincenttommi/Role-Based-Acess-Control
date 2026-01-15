from django.urls import path,include
from .views import StudentRegistrationView, UserRegistrationView,UserLoginView,UserLogoutView



urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('student/register/', StudentRegistrationView.as_view(), name='student-registration'),
]