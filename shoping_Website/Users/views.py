from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Customer
from admins.models import Products,Categorys,Companys
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
# # Create your views here.



def index(request):
    prods=Products.objects.all()
    return render(request,"user/index.html/",{'prods':prods})


def searchbar(request):
    query=request.GET.get('search')
    if query:
        cats=Categorys.objects.all().values()
        for d in cats:
            if str(query).lower()==str(d['name']).lower():
                query_id=d['id']
                prods=Products.objects.filter(category_id=query_id).values()
                return render(request,"user/index.html",{'prods':prods,'res':1})
        else:
            print("else")
            prods=Products.objects.all().values()
            return render(request,"user/index.html",{'prods':prods,'msg':"This Item Is Not Available"})
    else:
        prods=Products.objects.all().values()
        return render(request,"user/index.html",{'prods':prods,'msg':"Pls Enter Item Name"})

def shoping(request,id):
    print(id)
    obj=Products.objects.filter(category__exact=id)
    return render(request,"user/shop.html",{'prods':obj})
    
def toggle_view(request):
    return render(request,"user/toggle.html")
    cat=Categorys.objects.all()
    return render(request,"user/test.html",{'cats':cat})

def shop(request,id):
    print(id)
    pcart=request.session.get('cart',{})
    if request.method=="POST":
        pid=request.POST.get('addproduct')
        rm=request.POST.get('remove')
        if pcart:
            qty=pcart.get(pid)
            if qty:
                    if rm:
                        if qty<=1:
                            pcart.pop(pid)
                        else:
                            qty=qty-1
                            pcart[pid]=qty    
                    else:
                        qty=qty+1
                        pcart[pid]=qty
            else:
                pcart[pid]=1    
        else:
            pcart[pid]=1
        request.session['cart']=pcart
        print(request.session.get('cart'))
        return redirect('/')
    cid=request.GET.get('category')
    if cid:
        prods=Products.objects.filter(category=cid)
    else:
        prods=Products.objects.all()   
    cats=Categorys.objects.all()
    data={'prods':prods,'cats':cats}
    return render(request,"user/shop.html",data)





def signup_view(request):
    # return HttpResponse("hi")
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        father=request.POST.get('father')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        phone=request.POST.get('phone')
        img=request.FILES['imag']
        if str(pass1)==str(pass2):
            cobj=Customer(fname=fname,lname=lname,father=father,email=email,pass1=pass1,Phone=phone,image=img)
            # cobj.pass1=make_password(cobj.pass1)
            cobj.save()
            # return HttpResponse("Saved")
            return redirect('/')
        else:
            return HttpResponse("Password did not match")   
    return render(request,"user/signup.html")


def login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        if uname and upass:
            print(uname,upass)
            cust=Customer.objects.get(email=uname)   
            print(cust.email)
            print(cust.pass1)
            # return HttpResponse("Data fetched")
            if cust:
                print("if")
                if  str(upass)==str(cust.pass1):#check_password(upass,cust.pass1):
                    print("second if")
                    request.session['cust_id']=cust.id
                    print(cust.id)
                    request.session['cust_name']=cust.fname
                    request.session['cust_email']=cust.email
                    # url_image = cust.image
                    print("session set Successfully")
                    print(cust.image)
                    if cust.image:
                        request.session['cust_image']=cust.image.url
                    else:
                        request.session['cust_image']=""
                    return redirect('/')
            else:
                return redirect('/user/signup/')
        else:
            return render(request,"user/cust_login.html",{'msg':"Pls Enter Email And Pass "})
    return render(request,"user/cust_login.html")





def logout_view(request):
    request.session.clear()
    return redirect('/')

# @login_required(login_url='/userlogin/')
# def cart_view(request):
#     ids=[]
#     try:
#         ids=list(request.session.get('cart').keys())
#     except:
#         pass    
#     prods=Products.objects.filter(id__in=ids)
#     return render(request,"user/cart.html",{'prods':prods})

def profile_view(request):
    id=request.session.get('cust_id')    
    obj=Customer.objects.get(id=id)
    print(obj)
    return render (request,"user/profile.html",{'rec':obj})
b=[]
def view_product(requset):
    r=requset.session.get('cart')
    s=list(r)
    print(s)
    print(r)
    rec=Products.objects.filter(id__in=s)
    return render (requset,"user/viewproduct.html",{'value':rec,'count':r})


def guest_view(request):
    # return HttpResponse("hlo")
    return render (request,"user/guest_profile.html")


def edit_password(request,id):
    obj=Customer.objects.get(id=id)
    if request.method=="GET":
        cpass=request.GET.get('cpass')
        print(cpass)
    return HttpResponse("Edit Password")   
        # print(cpass,type(cpass))
        # print(obj.pass1,type(obj.pass1))
        # if obj.pass1==str(cpass):
        #     print("Success")
        # print("NOt Success")
    return HttpResponse("Edit Password")
    

def show(request):
    id=request.session.get('cust_name')
    em=request.session.get('cust_email')
    print(id,em)
    return HttpResponse("session Read")

def cart_view(request):
    return render(request,"user/cart.html")


def Cust_update(request,id):
    obj=Customer.objects.get(id=id)
    if request.method=="POST":
        obj.name=request.POST.get('name')
    return HttpResponse("")


def image_delete(request,id):
    cust=Customer.objects.get(id=id)
    cust.image.delete()
    cust.save()
    return redirect("/profile/")

def password_forget(request):
    pass

def change_password(request):
    pass
    
    































# def viewproduct_view(request):
#     # prods=Product.objects.all()
#     r=request.session.get('cust_id')
#     print(request.session.get('cust_email'))
#     print(r)
#     return render(request,'user/viewproduct.html')

# Create your views here.
# from django.shortcuts import render,redirect
# from django.http import HttpResponse,HttpResponseRedirect
# from .models import Category,Product,Customer
# import os
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password,check_password
# # Create your views here.
# def index(request):
    # pass
#     pcart=request.session.get('cart',{})
#     if request.method=="POST":
#         pid=request.POST.get('addproduct')
#         rm=request.POST.get('remove')
#         if pcart:
#             qty=pcart.get(pid)
#             if qty:
#                     if rm:
#                         if qty<=1:
#                             pcart.pop(pid)
#                         else:
#                             qty=qty-1
#                             pcart[pid]=qty    
#                     else:
#                         qty=qty+1
#                         pcart[pid]=qty
#             else:
#                 pcart[pid]=1    
#         else:
#             pcart[pid]=1
#         request.session['cart']=pcart
#         print(request.session.get('cart'))
#         return redirect('/')
#     cid=request.GET.get('category')
#     if cid:
#         prods=Product.objects.filter(category=cid)
#     else:
#         prods=Product.objects.all()   
#     cats=Category.objects.all()
#     data={'prods':prods,'cats':cats}
#     return render(request,"index.html",data)

# def admin_login(request):
#     if request.method=="POST":
#         uname=request.POST.get('username')
#         upass=request.POST.get('password')
#         if uname=='admin' and upass=='12345':
#             return redirect('/dashboard/')
#         else:
#             return HttpResponse("Invalid username or Password!!!")
#     return render(request,"admin_login.html")


# def dashboard_view(request):
#     return render(request,"dashboard.html")

# def addproduct_view(request):
#     if request.method=="POST":
#         pname=request.POST.get('name')
#         price=request.POST.get('price')
#         cat=request.POST.get('category')
#         des=request.POST.get('des')
#         img=request.FILES['imag']
#         cobj=Category.objects.get(id=cat)
#         pobj=Product(name=pname,price=price,category=cobj,des=des,image=img)
#         pobj.save()
#         return redirect('/viewproduct/')
#     cats=Category.objects.all()
#     return render(request,"addproduct.html",{'cats':cats})

# def viewproduct_view(request):
#     prods=Product.objects.all()
#     return render(request,'viewproduct.html',{'prods':prods})


# def deleteproduct_view(request,id):
#     rec=Product.objects.get(id=id)
#     rec.delete()
#     os.remove(rec.image.path)
#     return redirect('/viewproduct/')

# def addcategory_view(request):
#     if request.method=="POST":
#         cname=request.POST.get('name')
#         des=request.POST.get('des')
#         cobj=Category(name=cname,des=des)
#         cobj.save()
#     return render(request,"addcategory.html")

# def signup_view(request):
#     if request.method=="POST":
#         fname=request.POST.get('fname')
#         lname=request.POST.get('lname')
#         father=request.POST.get('father')
#         email=request.POST.get('email')
#         pass1=request.POST.get('pass1')
#         pass2=request.POST.get('pass2')
#         phone=request.POST.get('phone')
#         img=request.FILES['imag']
#         if pass1==pass2:
#             cobj=Customer(fname=fname,lname=lname,father=father,email=email,pass1=pass1,Phone=phone,image=img)
#             cobj.pass1=make_password(cobj.pass1)
#             cobj.save()
#             return redirect('/')
#         else:
#             return HttpResponse("Password did not match")   
#     return render(request,"signup.html")

# def userlogin_view(request):
#     if request.method=="POST":
#         uname=request.POST.get('username')
#         upass=request.POST.get('password')
#         cust=Customer.objects.get(email=uname)   
#         if cust:
#             if uname==cust.email and check_password(upass,cust.pass1):
#                 request.session['cust_id']=cust.id
#                 request.session['cust_name']=cust.fname
#                 request.session['cust_email']=cust.email
#                 return redirect('/')
#         else:
#             pass
#     return render(request,"userlogin.html")


# def logout_view(request):
#     request.session.clear()
#     return redirect('/')

# @login_required(login_url='/userlogin/')
# def cart_view(request):
#     ids=[]
#     try:
#         ids=list(request.session.get('cart').keys())
#     except:
#         pass    
#     prods=Product.objects.filter(id__in=ids)
#     return render(request,"cart.html",{'prods':prods})