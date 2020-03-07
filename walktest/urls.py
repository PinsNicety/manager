from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='walktest-home'),
    path('results/<int:id>', views.results, name='walktest-results'),
    path('<int:id>', views.export, name='walktest-export'),
    path('<str:site_name>', views.home_data, name='walktest-home_data'),

]
