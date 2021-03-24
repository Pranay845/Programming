from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home,name="Home"),
    path('About/', views.about,name="About"),
    path('Contact/', views.contact,name="Contact"),
    path('Search/', views.search, name="Search"),
    path('SignUp/', views.handleSignUp, name="handleSignUp"),
    path('Login/', views.handeLogin, name="handleLogin"),
    path('Logout/', views.handelLogout, name="handleLogout"),
]

