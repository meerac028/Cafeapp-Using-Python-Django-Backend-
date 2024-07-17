from django.shortcuts import render,redirect
from cafeapp.models import category_db,product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def cafe(request):
    return render(request,"index.html")
def add_category(request):
    return render(request,"Add_category.html")

def category_save(request):
    if request.method=="POST":
        a=request.POST.get('Category_name')
        b = request.POST.get('Description')
        c=request.FILES['profile_image']
        obj=category_db(Category_name=a,Description=b,profile_image=c)
        obj.save()
        return redirect(add_category)

def dis_category(request):
    data=category_db.objects.all()
    return render(request,"display_category.html",{'data':data})

def edit_cat(request,d_id):
    var = category_db.objects.get(id=d_id)
    return render(request,"edit_category.html",{'var':var})
#
def update_cat(request,d_id):
    if request.method=="POST":
        a = request.POST.get('Category_name')
        b = request.POST.get('Description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = category_db.objects.get(id=d_id).profile_image
        category_db.objects.filter(id=d_id).update(Category_name=a,Description=b,profile_image=file)
        return redirect(dis_category)
#

def delete_cat(request,d_id):
    data=category_db.objects.filter(id=d_id)
    data.delete()
    return redirect(dis_category)


def add_product(request):
    cat=category_db.objects.all()
    return render(request,"pro_add.html",{'cat':cat})

def product_save(request):
    if request.method=="POST":
        a=request.POST.get('Category_name')
        b = request.POST.get('product_name')
        c = request.POST.get('Description')
        d = request.POST.get('price')
        e =request.FILES['product_image']
        obj=product_db(Category_name=a, product_name=b,  description=c, price=d, product_image=e)
        obj.save()
        return redirect( add_product)


def dis_product(request):
    data=product_db.objects.all()
    return render(request,"pro_dis.html",{'data':data})

def edit_product(request,d_id):
    cat = product_db.objects.all()
    var = product_db.objects.get(id=d_id)
    return render(request,"pro_edit.html",{'var':var,'cat':cat})

def update_product(request,d_id):
    if request.method=="POST":
        a = request.POST.get('Category_name')
        b = request.POST.get('product_name')
        c = request.POST.get('Description')
        d = request.POST.get('price')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = product_db.objects.get(id=d_id).product_image
        product_db.objects.filter(id=d_id).update(Category_name=a,product_name=b,description=c,price=d,product_image=file)
        return redirect(dis_product)

def delete_product(request,d_id):
    data=product_db.objects.filter(id=d_id)
    data.delete()
    return redirect(dis_product)

def admin_login(request):
    return render(request,"admin_login.html")

def login_save(request):
    if request.method=="POST":
        a=request.POST.get("username")
        c = request.POST.get("password")
        if User.objects.filter(username__contains=a).exists():
            x=authenticate(username=a,password=c)
            if x is not None:
                login(request,x)
                request.session['username']=a
                request.session['password']=c


                return redirect(cafe)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)