from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_firstapp, name='all_firstapp'),
   path('<int:app_id>/', views.app_detail, name='app_details'),
   path('app_Stores/', views.app_store_views, name='app_store_views'),
   
]