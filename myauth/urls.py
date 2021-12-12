from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .import views

urlpatterns = [
    path('login',views.login),
    path('',views.index),
]
