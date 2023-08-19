from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import SalesOrder
from Customers.models import Customer
# Create your views here.
def add_sales_order(request:HttpRequest):
    ID=request.GET.get("CUSTOMER_ID")
    customer=Customer.objects.get(CUSTOMER_ID = ID)
    s=SalesOrder(CUSTOMER_ID = customer, AMOUNT = request.GET.get("AMOUNT"))
    s.save()
    return HttpResponse("Hello sales order")