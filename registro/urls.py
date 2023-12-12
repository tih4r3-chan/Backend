from django.urls import path
from .views import user_registration

urlpatterns = [
    path('', user_registration, name='registro'),
]
