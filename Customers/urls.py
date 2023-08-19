from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('addCustomer', views.addCustomer),
    path('delCustomer',views.delCustomer)
]