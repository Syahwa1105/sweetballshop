import datetime
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    """Render awal halaman utama (boleh render karena bukan bagian CRUD)."""
    filter_type = request.GET.get("filter", "all")
    category = request.GET.get("category", None)

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    if category:
        products = products.filter(category=category)

    context = {
        "npm": "2406437533",
        "nama": request.user.username,
        "kelas": "PBP-B",
        "products": products,
        "last_login": request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)


# CREATE PRODUCT (AJAX) 
@login_required(login_url='/login')
def add_product(request):
    """Handle create product 100% via AJAX."""
    if request.method != 'POST':
        return JsonResponse({
            "status": "error",
            "message": "Gunakan POST untuk menambah produk."
        }, status=400)

    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return JsonResponse({
            "status": "success",
            "message": "Produk berhasil ditambahkan!",
            "product": {
                "id": str(product.id),
                "name": product.name,
                "price": product.price,
                "category": product.category,
                "thumbnail": product.thumbnail,
                "description": product.description,
            }
        })
    else:
        return JsonResponse({
            "status": "error",
            "message": "Form tidak valid.",
            "errors": form.errors
        }, status=400)


# DETAIL PRODUCT (AJAX)
@login_required(login_url='/login')
def product_detail(request, pk):
    """Return detail produk sebagai JSON untuk modal detail."""
    product = get_object_or_404(Product, pk=pk)
    return JsonResponse({
        "id": str(product.id),
        "name": product.name,
        "price": product.price,
        "category": product.category,
        "description": product.description,
        "thumbnail": product.thumbnail,
        "is_featured": product.is_featured,
        "user": product.user.username,
    })


# JSON / XML (READ MULTIPLE)
def products_json(request):
    filter_type = request.GET.get('filter')
    category = request.GET.get('category')

    qs = Product.objects.all()

    if filter_type == 'my':
        if request.user.is_authenticated:
            qs = qs.filter(user=request.user)
        else:
            qs = Product.objects.none()

    if category:
        qs = qs.filter(category=category)

    data = serializers.serialize("json", qs)
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


# REGISTER (AJAX)
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if form.is_valid():
                form.save()
                return JsonResponse({
                    "status": "success",
                    "message": "Akun berhasil dibuat!"
                })
            else:
                return JsonResponse({
                    "status": "error",
                    "message": "Registrasi gagal. Pastikan semua field diisi dengan benar.",
                    "errors": form.errors
                }, status=400)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')

    return render(request, 'register.html', {'form': form})


# LOGIN (AJAX)
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = JsonResponse({"status": "success", "message": "Login berhasil!"})
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                return JsonResponse({
                    "status": "error",
                    "message": "Username atau password salah!"
                }, status=400)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})


# LOGOUT (AJAX)
def logout_user(request):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        logout(request)
        response = JsonResponse({"status": "success", "message": "Logout berhasil!"})
        response.delete_cookie("last_login")
        return response

    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie('last_login')
    return response


# EDIT PRODUCT (AJAX)
@login_required(login_url='/login')
def edit_product(request, pk):
    """Handle update product full AJAX."""
    product = get_object_or_404(Product, pk=pk)

    if product.user != request.user:
        return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)

    if request.method == "GET":
        
        return JsonResponse({
            "id": str(product.id),
            "name": product.name,
            "price": product.price,
            "category": product.category,
            "thumbnail": product.thumbnail,
            "description": product.description,
        })

    elif request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": "success",
                "message": "Produk berhasil diupdate!"
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "Form tidak valid.",
                "errors": form.errors
            }, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)


# DELETE PRODUCT (AJAX)
@login_required(login_url='/login')
def delete_product_ajax(request, pk):
    """Hapus produk full AJAX."""
    product = get_object_or_404(Product, pk=pk)

    if product.user != request.user:
        return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)

    if request.method == "DELETE":
        product.delete()
        return JsonResponse({"status": "success", "message": "Produk berhasil dihapus!"})

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

@csrf_exempt
def create_product_flutter(request):
    if request.method != "POST":
        return JsonResponse(
            {"status": False, "message": "Invalid method"},
            status=400,
        )

    try:
        data = request.POST 
        username = data.get("username", "").strip()
        if not username:
            return JsonResponse(
                {"status": False, "message": "Missing username"},
                status=400,
            )

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse(
                {"status": False, "message": "User not found"},
                status=400,
            )


        name = data.get("name", "").strip()
        price_raw = data.get("price", "").strip()
        description = data.get("description", "").strip()
        thumbnail = data.get("thumbnail", "").strip()
        category = data.get("category", "").strip()
        is_featured_str = data.get("is_featured", "false")

        if not name or not price_raw:
            return JsonResponse(
                {"status": False, "message": "Name dan price wajib diisi"},
                status=400,
            )

        try:
            price = int(price_raw)
        except ValueError:
            return JsonResponse(
                {"status": False, "message": "Price harus berupa angka"},
                status=400,
            )

        product = Product.objects.create(
            user=user,
            name=name,
            price=price,
            description=description or "",
            thumbnail=thumbnail or "",
            category=category or "shoes",
            is_featured=is_featured_str.lower() == "true",
        )

        return JsonResponse(
            {
                "status": True,
                "message": "Product berhasil dibuat!",
                "id": str(product.id),
            }
        )

    except Exception as e:
        return JsonResponse(
            {
                "status": False,
                "message": f"Server error: {str(e)}",
            },
            status=500,
        )

@csrf_exempt
def flutter_logout(request):
    if request.method != "POST":
        return JsonResponse({"status": False, "message": "Invalid method"}, status=400)

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = ""

    logout(request)

    return JsonResponse({
        "status": True,
        "username": username,
        "message": "Logged out successfully!"
    })
