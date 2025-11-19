from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout   # <-- WAJIB ADA
from django.views.decorators.csrf import csrf_exempt


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def login_flutter(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": True,
                "message": "Login success",
                "username": username,   # <- PENTING: KIRIM BALIK USERNAME
            })
        else:
            return JsonResponse({
                "status": False,
                "message": "Invalid credentials",
            })
    return JsonResponse({
        "status": False,
        "message": "Invalid method",
    })

@csrf_exempt
def logout_flutter(request):
    logout(request)
    return JsonResponse({"status": True, "message": "Logged out"})


@csrf_exempt
def register_flutter(request):
    if request.method != "POST":
        return JsonResponse({"status": False, "message": "Invalid method"}, status=400)

    username = request.POST.get("username")
    password = request.POST.get("password")

    if not username or not password:
        return JsonResponse({"status": False, "message": "Missing fields"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"status": False, "message": "Username already exists"}, status=400)

    User.objects.create_user(username=username, password=password)

    return JsonResponse({"status": True, "message": "Register successful!"})
