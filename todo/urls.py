from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('edit/<int:todo_id>/', views.todo_edit, name='todo_edit'),
    path('delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
]
