# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Display registration or login form based on user authentication status
    path('home/', views.home, name='home'),
    path('table/', views.table, name='table'),  # Display the table for logged-in users
    path('add/', views.add, name='add'),   # Add new entries
    path('edit/<int:pk>/', views.edit, name='edit'),  # Edit individual entries
    path('delete/<int:pk>/', views.delete, name='delete'),  # Delete individual entries
    path('edit_table/', views.edit_table, name='edit_table'),
    path('download_statement/', views.download_statement, name='download_statement'),
    path('statement_form/', views.statement_form, name='statement_form'),
    path('register/', views.register, name='register'),  # Register form
    path('login/', views.user_login, name='login'),  # Login form
]
