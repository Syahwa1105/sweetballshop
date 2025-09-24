#TI_4
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm


@login_required(login_url='/login') #TI_4
def show_main(request): # isi dari sebelum nya diubah untuk TI_4
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    context = {
        "npm": "2406437533",
        "nama": request.user.username,   # username dari user yang login
        "kelas": "PBP-B",
        "products": products,
        "last_login": request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

#TI_3 dan diubah ke karena TI_4
@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)   
        product.user = request.user         
        product.save()                      
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "product_form.html", context)

@login_required(login_url='/login')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})

# (JSON/XML)
def products_json(request):
    data = serializers.serialize("json", Product.objects.all())
    return HttpResponse(data, content_type="application/json")

def products_xml(request):
    data = serializers.serialize("xml", Product.objects.all())
    return HttpResponse(data, content_type="application/xml")

def product_json_by_id(request, pk):
    data = serializers.serialize("json", [get_object_or_404(Product, pk=pk)])
    return HttpResponse(data, content_type="application/json")

def product_xml_by_id(request, pk):
    data = serializers.serialize("xml", [get_object_or_404(Product, pk=pk)])
    return HttpResponse(data, content_type="application/xml")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#TI_4 
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response