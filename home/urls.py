from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='Contact'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='Search'),
    path('signup/', views.handleSignUp, name='handleSignUp'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
]
