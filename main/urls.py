from django.urls import path
from main import views
#TI_4
from main.views import register
from main.views import login_user
from main.views import logout_user

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    #TI_3
    path('products/add/', views.add_product, name='add_product'),
    path('products/<uuid:pk>/', views.product_detail, name='product_detail'),
    path('json/', views.products_json, name='products_json'),
    path('xml/', views.products_xml, name='products_xml'),
    path('json/<uuid:pk>/', views.product_json_by_id, name='product_json_by_id'),
    path('xml/<uuid:pk>/', views.product_xml_by_id, name='product_xml_by_id'),
    #TI_4
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    #TI_5
    path('products/<uuid:pk>/edit/', views.edit_product, name='edit_product'),
    path('products/<uuid:pk>/delete/', views.delete_product, name='delete_product'),

]
