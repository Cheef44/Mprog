from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_filter, name='post_list'),
    path('post/<int:id>/detail/', views.post_detail, name='post_detail'),
]
