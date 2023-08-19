from django.db import models
from Customers.models import Customer
# Create your models here.
class SalesOrder(models.Model):
    SALES_ORDER_ID=models.AutoField(primary_key=True)
    CUSTOMER_ID=models.ForeignKey(Customer,on_delete=models.CASCADE,db_column="CUSTOMER_ID")
    AMOUNT=models.IntegerField()