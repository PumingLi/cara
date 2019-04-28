from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('add_options/', views.add_options, name='add_options'),
]
