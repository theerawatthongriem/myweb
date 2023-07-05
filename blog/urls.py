from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('dashboard',base),
    path('register',reg),
    path('login',log),
    path('logout',logt),
    path('profile',profile),
    path('editprofile',updateprofile),
    path('history',history),
]