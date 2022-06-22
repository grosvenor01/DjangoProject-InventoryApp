from itertools import count
from django.shortcuts import render,get_object_or_404,redirect
from .models import order,product,staff,profile
from .forms import formProduct
# Create your views here.
def index(request):
    context={
        'order':order.objects.count(),
        'product':product.objects.count(),
        'staff': staff.objects.count()
    }
    return render(request,'pages/index.html',context)
 
def ordering(request):
    context={
        'order':order.objects.count(),
        'product':product.objects.count(),
        'staff': staff.objects.count(),
        'ord' : order.objects.all(),
        'prd' : product.objects.all(),
        'stf' : staff.objects.all(),
    }
    return render(request,'pages/order.html',context)

def producting(request):
    
    if request.method=="POST":
        add_product=formProduct(request.POST , request.FILES)
        if add_product.is_valid():
            add_product.save()
    context={
        'order':order.objects.count(),
        'product':product.objects.count(),
        'staff': staff.objects.count(),
        'ord' : order.objects.all(),
        'prd' : product.objects.all(),
        'stf' : staff.objects.all(),
        'form' : formProduct() 
    }
    return render(request,'pages/product.html',context)

def staffing(request):
    context={
        'order':order.objects.count(),
        'product':product.objects.count(),
        'staff': staff.objects.count(),
        'ord' : order.objects.all(),
        'prd' : product.objects.all(),
        'stf' : staff.objects.all(),
    }
    return render(request,'pages/staff.html',context)

def profiling(request,id):
    context={
        'profile':get_object_or_404(profile, id=id)
    }
    return render(request,'pages/profile.html',context)

def staff_index(request,):
    return render(request,'pages/staff_index.html')

def delete(request,id):
    if request.method=="POST":
        delete_product=get_object_or_404(product , id = id)
        delete_product.delete()
        return redirect('/')
    return render(request,'pages/delete.html')