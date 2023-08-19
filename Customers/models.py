from django.db import models

# Create your models here.
class Customer(models.Model):
    CUSTOMER_ID=models.AutoField(primary_key=True)
    COMPANY_NAME=models.CharField(max_length=35,unique=True)

