from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path('cuenta/', UserRegistrationView.as_view(), name='user_registration'),
]
