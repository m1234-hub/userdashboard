from django.urls import path
from dash import views


urlpatterns = [
    path('', views.signup, name='register')
]