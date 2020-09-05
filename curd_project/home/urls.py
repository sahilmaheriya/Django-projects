from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('delete/<int:id>/', views.delete_data, name = "delete"),
    path('update/<int:id>/', views.update_data, name = "update")
]
