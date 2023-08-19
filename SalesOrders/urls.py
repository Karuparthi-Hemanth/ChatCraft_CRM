from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('addsalesorder', views.add_sales_order)
]