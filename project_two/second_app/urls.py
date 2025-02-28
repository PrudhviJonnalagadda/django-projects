from django.urls import path
from second_app import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('help/', views.help, name='help')
]