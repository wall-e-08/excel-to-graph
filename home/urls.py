from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('data-sheet/<int:ds_id>', views.data_sheet, name='data_sheet'),
    path('select-data/<int:ds_id>', views.select_data, name='select_data'),
    path('ajax-save-xy-data', views.ajax_save_xy_data, name='ajax_save_xy_data'),
]