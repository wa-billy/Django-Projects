
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register),
    path('login/', views.login),
    path('todo/', views.todo),
    path('logout/', views.logout, name='signout')
]
