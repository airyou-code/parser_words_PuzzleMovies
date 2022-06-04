from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('lesson/<int:pk>/edit', views.editlesson),
    path('lesson/<int:pk>/addword/<int:id>', views.addword),
    # path('update', views.update),
]
