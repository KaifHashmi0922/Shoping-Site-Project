from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from admins.models import Products,Categorys,Admin,Companys
from Users.models import Customer
from django.http import HttpResponse,HttpResponseRedirect
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password



# <---  Start Admin Home Page --->

# def home_view(request):
#     cid=request.GET.get('category')
#     if cid:
#         prods=Products.objects.filter(category=cid)
#     else:
#         prods=Products.objects.all()   
#     cats=Categorys.objects.all()
#     data={'prods':prods,'cats':cats}
#     return render(request,"admins/index.html",data)

# <--- End Admin Home Page --->

#==================================================================================================================


#  # <--- Start Admin Login Page   If more then One --->

def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        rec=Admin.objects.all()
        for data in rec:          
            if data.uname==str(uname) and data.password==str(upass):
                return redirect('/admins/dashboard/')
        else:
            return HttpResponse("Invalid username or Password!!!")
    return render(request,"admins/admin_login.html")

# # <--- End Admin Login Page --->

# #==================================================================================================================

#  # <--- Start  Admin Management Page --->
 
def dashbord_view(request):
    return render(request,"admins/dashbord.html")

# # <--- End  Admin Management Page --->

# #==================================================================================================================



# # <--- Start  Category Management Page --->


# # <---  Start Add Category  Page --->

def addcategory_view(request):
    if request.method=="POST":
        cname=request.POST.get('name')
        des=request.POST.get('des')
        image=request.FILES['image']
        cobj=Categorys(name=cname,des=des,image=image)
        cobj.save()
    return render(request,"admins/addcategory.html")

# # <--- End Add Category  Page --->p


# # <--- Start View Category  Page --->

def category_view(request):
    obj=Categorys.objects.all()
    return render (request,'admins/category_view.html',{'rec':obj})

# # <--- End  View Category  Page --->


# # <--- Start Edit Category  Page --->

def edit_category(request,id):
    rec=Categorys.objects.get(id=id)
    if request.method=="POST":
        rec.name=request.POST.get('name')
        rec.des=request.POST.get('des')
        if request.FILES['image']:
            os.remove(rec.image.path)
            rec.image.delete()
            rec.image=request.FILES['image']
        rec.save()
        return redirect('/admins/view_categorys/')
    return render (request,"admins/category_edit.html/",{'rec':rec})

# # <--- End Edit Category  Page --->

# # <--- Start Delete Category  Page --->

def delete_category(request,id):
    obj=Categorys.objects.get(id=id)
    obj.delete()
    os.remove(obj.image.path)
    return redirect('/admins/view_categorys/')

# # <--- End Delete Category  Page --->

def add_comp(request):
    # return render (request,"admins/add_comp.html")
    if request.method=="POST":
        cname=request.POST.get('cname')
        cat=request.POST.get('category')
        ptype=request.POST.get('ptname')
        image=request.FILES['image']
        cobj=Categorys.objects.get(id=cat)
        comp=Companys.objects.create(name=cname,types=cobj,c_info=ptype,image=image)
        return redirect("/admins/view_companys/")
    cats=Categorys.objects.all()
    return render (request,"admins/add_comp.html",{'cats':cats})
        
def company_view(request):
    rec=Companys.objects.all()
    return render (request,'admins/company_view.html',{'rec':rec})


def edit_company(request,id):
    obj=Companys.objects.get(id=id)
    if request.method=="POST":
        obj.name=request.POST.get('cname')
        cat=request.POST.get('category')
        obj.c_info=request.POST.get('ptype')
        obj.types=Categorys.objects.get(id=cat)
        if request.FILES['image']:
            os.remove(obj.image.path)
            obj.image.delete()
            obj.image=request.FILES['image']
        obj.save()
        return redirect('/admins/view_companys/')
    cats=Categorys.objects.all()
    return render (request,"admins/company_edit.html/",{'rec':obj,'cats':cats})
        
def delete_company(reques,id):
    rec=Companys.objects.get(id=id)
    rec.delete()
    os.remove(rec.image.path)
    return redirect("/admins/view_companys/")
    

# #==================================================================================================================
# # <--- Start Productss Management  Page --->


# # <--- Start Add Productss  Page --->


def addproduct(request):
    if request.method=="POST":
        pname=request.POST.get('name')
        price=request.POST.get('price')
        cat=request.POST.get('category')
        des=request.POST.get('des')
        img=request.FILES['imag']
        cobj=Categorys.objects.get(id=cat)
        pobj=Products(name=pname,price=price,category=cobj,des=des,image=img)
        pobj.save()
        return redirect('/admins/admins_viewproduct/')
    cats=Categorys.objects.all()
    return render(request,"admins/addproduct.html",{'cats':cats})

# # <--- End  Add Productss  Page --->

# # <--- Start View Productss  Page --->

def admin_viewproduct(request):
    prods=Products.objects.all()
    return render(request,'admins/admin_viewproduct.html',{'prods':prods})

# # <--- End  View Productss  Page --->

# # <--- Start Edit Productss  Page --->

def edit_product(request,id):
    obj=Products.objects.get(id=id)
    if request.method=="POST":
        obj.name=request.POST.get('name')
        obj.price=request.POST.get('price')
        # obj.category=request.POST.get('category')
        obj.des=request.POST.get('des')
        if request.FILES['imag']:
            os.remove(obj.image.path)
            obj.image.delete()
            obj.image=request.FILES['imag']
        obj.save()
        return redirect('/admins/admin_viewproduct/')
    cats=Categorys.objects.all()
    return render (request,"admins/product_edit.html/",{'cats':cats,'rec':obj})
    
    
# # <--- End Edit Productss  Page --->

# # <--- Start Delete Productss  Page --->

def delete_product(request,id):
    rec=Products.objects.get(id=id)
    rec.delete()
    os.remove(rec.image.path)
    return redirect('/admins/admins_viewproduct/')

# # <--- End Delete Products  Page --->

# # <--- End Products Management  Page --->

# #==================================================================================================================

# # <--- Start Custmer Mangement Page --->

# # <--- Start View  Custmert Page --->

def view_custmer(request):
    rec=Customer.objects.all()
    return render(request,"admins/customer_view.html",{'rec':rec})

# # <--- End View  Custmert Page --->

# #==================================================================================================================


# # <--- Start Search Bar Management --->



# def question(request):
#     # print(request.GET.get('question'))
#     print("hlo")
#     return HttpResponse("hloe")
   
#     if request.method=="POST":
#         q=request.GET.get('question')
#         s=Category.objects.get(name=q)
#         print(s.name)
#         if q:
#             prods=Products.objects.filter(name=s.name)
#         else:
#             prods=Productss.objects.all()   
#         cats=Category.objects.all()
#         data={'prods':prods,'cats':cats}
#         return render(request,"admin/home.html",data)
#     else:
#         print("else")
#         return redirect('/admin/home/')
    




# # <--- End Search Bar Management --->
    
    
# #==================================================================================================================