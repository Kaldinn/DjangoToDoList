from django.urls import path
from . import views


#URL Config
urlpatterns = [
    path('tasks/', views.task_page, name='list'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete/<str:pk>/', views.delete_task, name='delete'),
    path('', views.login_page, name='login'),
    path('register/', views.register_page, name='register')
]