from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todos_list, name='todos_list'),
    path('new/', views.new_todo, name='new_todo'),
    path('todo/<int:pk>/', views.detail, name='detail'),
    path('todo/<int:pk>/delete/', views.delete, name='delete'),
    path('todo/<int:pk>/edit/', views.edit_todo, name='edit'),
]