from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_firstapp, name='all_firstapp'),
]
