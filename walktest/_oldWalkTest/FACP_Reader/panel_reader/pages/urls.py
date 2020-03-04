from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_complete', views.test_complete, name='test_complete')
]