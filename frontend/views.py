from django.shortcuts import render
from cafeapp.models import product_db,category_db

# Create your views here.
def index_fro(request):
    pro=product_db.objects.all()
    cat=category_db.objects.all()
    return render(request,"index_front.html",{'pro':pro,'cat':cat})

def about_fro(request):
    return render(request,"about.html")

def contact_fro(request):
    return render(request,"contact.html")


def product_fro(request,cat_name):
    pro=product_db.objects.filter(Category_name=cat_name)
    return render(request,"products_fro.html",{'pro':pro})

