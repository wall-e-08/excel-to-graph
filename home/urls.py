from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('show-data', views.all_data, name='all_data'),
]