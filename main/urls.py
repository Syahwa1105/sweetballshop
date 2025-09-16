from django.urls import path
from main import views

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
]
