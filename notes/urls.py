from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='notes-home'),
    path('<str:organization_name>/', views.organization, name='notes-organization'),
    path('<str:organization_name>/<str:site_name>/', views.site, name='notes-site')
]
