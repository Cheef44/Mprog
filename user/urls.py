from django.urls import path, include
from . import views

urlpatterns = [
    path('user/logout/', views.user_logout, name='user_logout'),
    path('user/<int:id>/', views.user_accaunt, name='user_accaunt'),
    path('user/login/', views.user_login, name='user_login'),
    path('user/registration/', views.user_registration, name='user_registration'),
]