from django.urls import path
from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, show_product, create_product, create_car, register_user, login_user, logout_user, edit_product, delete_product, add_product_entry_ajax, edit_product_entry_ajax, login_ajax, register_ajax, proxy_image, create_product_flutter, get_my_products_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-car/', create_car, name='create_car'),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product-entry-ajax/<uuid:id>/', edit_product_entry_ajax, name='edit_product_entry_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('my-products-json/', get_my_products_json, name='get_my_products_json'),
]