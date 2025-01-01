from django.contrib import admin
from .models import Products,Categorys,Admin,Companys
from Users.models import Customer
# Register your models here.

#  Admin Table

class admins_view(admin.ModelAdmin):
    list_display=('id','uname','password')
admin.site.register(Admin,admins_view)
#-----------------------------------------


class Category_view(admin.ModelAdmin):
    list_display=('id','name','feature')
admin.site.register(Categorys,Category_view)

#-----------------------------------------

class Company_view(admin.ModelAdmin):
    list_display=('id','name','types','image')
admin.site.register(Companys,Company_view)

#-----------------------------------------

class Product_view(admin.ModelAdmin):
    list_display=('id','name','category','company','price','des','image')
admin.site.register(Products,Product_view)

#--------------------------------------------

class Customer_view(admin.ModelAdmin):
    list_display=('id','fname','lname','father','email','Phone','pass1','image')
    
admin.site.register(Customer,Customer_view)
