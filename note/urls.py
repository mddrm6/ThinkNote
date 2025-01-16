from django.urls import path

from . import views

app_name = 'note'

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('new/', views.new_note, name='new_note'),
    path('note/<int:pk>/', views.detail, name='detail'),
    path('note/<int:pk>/delete/', views.delete, name='delete'),
    path('note/<int:pk>/edit/', views.edit_note, name='edit'),
]