from django.shortcuts import render

def show_main(request):
    context = {
        "npm": "2406437533",      
        "nama": "Qoriana Syahwa Maharani",     
        "kelas": "PBP-B "  
    }
    return render(request, "main.html", context)
