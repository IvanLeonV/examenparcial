from django.urls import path
from . import views

app_name='tareasApp'

urlpatterns=[
    path('',views.Vprincipal,name='Vprincipal'),

    path('Ntarea',views.Ntarea,name='Ntarea'),
   
]