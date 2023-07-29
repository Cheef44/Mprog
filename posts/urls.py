from django.urls import path, include
from . import views

urlpatterns = [
    path('user/login/', views.user_login, name='user_login'),
    path('user/registration/', views.user_registration, name='user_registration'),
    path('post/create/<int:id>', views.post_edit, name='post_editor'),
    path('post/<int:id>/detail/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_creater'),
    path('', views.post_filter, name='post_list'),
    
]
