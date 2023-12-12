from django.urls import path
from django.contrib.auth import views as  auth_views
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'), #hecho 
    # path('logout/', views.user_logout, name='logout')
]