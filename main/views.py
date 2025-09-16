from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm


def show_main(request):
    products = Product.objects.all() 
    context = {
        "npm": "2406437533",
        "nama": "Qoriana Syahwa Maharani",
        "kelas": "PBP-B",
        "products": products, 
    }
    return render(request, "main.html", context)

#TI_3
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:show_main")
    else:
        form = ProductForm()
    return render(request, "product_form.html", {"form": form})

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
