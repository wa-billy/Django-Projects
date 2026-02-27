
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register),
    path('login/', views.login),
    path('todo/', views.todo),
    path('logout/', views.logout, name='signout'),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>', views.delete_todo)
]
