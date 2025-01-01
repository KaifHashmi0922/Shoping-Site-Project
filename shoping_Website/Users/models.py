from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Customer(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    father=models.CharField(max_length=100)
    email=models.EmailField()
    pass1=models.CharField(max_length=100)
    Phone=models.CharField(max_length=10)
    image=models.FileField(upload_to="uploads/users/",null=True)
    
