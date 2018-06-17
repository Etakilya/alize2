from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include,url



urlpatterns = [
    path('', views.index, name="index"),
    path('category', views.category, name="category"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('Pizza', views.pizza, name="Pizza"),
    path('Salad', views.salad, name="Salad"),
    path('Steak', views.steak, name="Steak"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('reg', views.reg, name="reg"),
    path('user', views.user, name="user"),
	path('edit', views.edit, name="edit"),
	path('teacher', views.teacher, name="teacher"),
] 
