from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showopdrx,name='showopdrx'),
    path('Insertopdrx/<int:UHIDid>', views.Insertopdrx,name='Insertopdrx'),
    path('Edit/<int:id>', views.Editopdrx,name='Editopdrx'),
    path('Update/<int:id>', views.updateopdrx,name='updateopdrx'),
    # path('Delete/<int:id>', views.Delopdcomplain,name='Delopdcomplain'),
]