from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('read/<int:blog_id>/', views.read, name='read'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
]