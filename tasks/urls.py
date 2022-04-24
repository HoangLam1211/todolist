from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name = 'list'),
    path('update/<str:pk>', updateTask, name= 'update_task'),
    path('delete/<str:pk>', deleteTask, name= 'delete'),
]
