from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = "home"),
    path('update/<int:id>/',views.update, name = "update"),
    path('delete/<int:id>/', views.delete_data, name= "delete"),
]