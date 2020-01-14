from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='timekeeper-home'),
    path('entries/', views.entries, name='timekeeper-entries'),
    path('expenses/', views.expenses, name='timekeeper-expenses'),
]
