from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('update/', views.update),
    path('user/', include('user.urls'))
]
