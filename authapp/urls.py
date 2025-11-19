from django.urls import path
from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.login_flutter, name='login_flutter'),
    path('register/', views.register_flutter, name='register_flutter'),
    path('logout/', views.logout_flutter, name='logout_flutter'),
]
