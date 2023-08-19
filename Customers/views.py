from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Customer
# Create your views here.
def addCustomer(request : HttpRequest):
    c=Customer(COMPANY_NAME = request.GET.get("COMPANY_NAME"))
    c.save()
    return HttpResponse("added customer")
def delCustomer(request : HttpRequest):
    c=Customer.objects.get(CUSTOMER_ID = request.GET.get("CUSTOMER_ID"))
    c.delete()
    return HttpResponse("deleted customer")
