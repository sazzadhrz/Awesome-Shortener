from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='indexView'),
    path('ok/', views.ok),
    path('test/', views.test, name='test'),
    path('<str:short_url>/stats', views.stats, name='stats'),
    path('generate/', views.generate, name='generate')
]
