from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.about),
    path('hello/<str:username>', views.hello),
    path('proyects/', views.projects),
    # path('tasks/<int:id>', views.tasks),
    path('tasks/', views.tasks),
    path('create_task/', views.create_task),
    path('create_project/', views.create_project),
]