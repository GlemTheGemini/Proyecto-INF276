"""
URL configuration for gimnasio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gym_app.views import home
from reserva.views import reserva, guardar_reserva, reserva_confirmed
from login.views import login_user, logout_user, register_user



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),



    #Reserva
    path('reserva', reserva, name='reserva'),
    path('guardar_reserva/', guardar_reserva, name='guardar_reserva'),
    path('reserva_confirmed', reserva_confirmed, name='reserva_confirmed'),



    #Login
    path('login', login_user, name='login'),
    path('logout', logout_user, name = "logout"),
    path('register_user', register_user, name='register_user'),




]
