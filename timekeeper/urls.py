from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='timekeeper-home'),
    path('entries/', views.entries, name='timekeeper-entries'),
    path('entries_export/<str:table_month>/', views.entries_export, name='entries_export'),
    path('expenses/', views.expenses, name='timekeeper-expenses'),
    path('expenses_export/<str:table_month>', views.expenses_export, name='expenses_export')
]
