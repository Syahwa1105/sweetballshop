from django.urls import path 
from main import views 

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<uuid:pk>/detail/', views.product_detail, name='product_detail'), 

    # JSON / XML
    path('products/json/', views.products_json, name='products_json'),
    path('xml/', views.products_xml, name='products_xml'),
    path('json/<uuid:pk>/', views.product_json_by_id, name='product_json_by_id'),
    path('xml/<uuid:pk>/', views.product_xml_by_id, name='product_xml_by_id'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # CRUD Product (AJAX only)
    path('products/<uuid:pk>/edit/', views.edit_product, name='edit_product'),
    path('products/<uuid:pk>/delete/ajax/', views.delete_product_ajax, name='delete_product_ajax'),
]
