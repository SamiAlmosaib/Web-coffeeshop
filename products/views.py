from django.shortcuts import get_object_or_404, render
from datetime import datetime
from .models import Product

# Create your views here.
def products(request):
    pro=Product.objects.all()
    name=None
    if 'searchname' in request.GET:
        name=request.GET['searchname']
        if name:
            pro=pro.filter(name__icontains=name)
    context={
         'products':pro
        
    }
    return render(request,'products/products.html',context)
def product(request, pro_id):
    context={
        'pro':get_object_or_404(Product, pk=pro_id)#what is it mean?
    }
    return render(request,'products/product.html',context)
def search (request):
    return render(request,'products/search.html')