from django.urls import path, include
from . import views

urlpatterns = [
    path('user/login/', views.user_login, name='user_login'),
    path('user/registration/', views.user_registration, name='user_registration'),
]