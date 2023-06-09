from django.contrib import admin
from django.urls import path , include 
from . import views 

urlpatterns = [
    path('', views.index , name='index'),
    path('new', views.create_view , name='create_view'),
    path('list', views.list_view , name ='list_view '),
    path('<id>/update', views.update_view , name='update_view'),
    path('<id>/delete', views.delete_view , name='delete_view'),
    path('adminpage', views.adminpage , name='adminpage'),
    
]