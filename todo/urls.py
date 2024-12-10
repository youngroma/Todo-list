from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('', views.all_tasks, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
