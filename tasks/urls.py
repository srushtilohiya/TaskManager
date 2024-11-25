from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
     path('send-invites/', views.send_invitations_view, name='send_invitations'),
]
