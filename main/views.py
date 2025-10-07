from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.models import Product
from main.models import Employee
from main.forms import ProductForm, CarForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.contrib.auth.models import User, update_last_login


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    context = {
        'name':'Raihana Auni Zakia',
        'class': 'PBP D',
        'npm': '2406495760',
        'product_list': product_list,
        'last_login': request.user.last_login,
        'user_login':request.user.username
    }

    return render(request, "main.html", context)

def add_employee(request):
    employee = Employee.objects.create(name='Raihana Auni Zakia', age='18', persona='mahasiswa')
    
    return HttpResponse(employee.name, employee.age, employee.persona)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')


    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def create_car(request):
    form = CarForm(request.POST or None)
    
    if form.is_valid() and request.method=="POST":
        form.save()
        return redirect("main:show_main")
    
    context = {'form': form}
    return render(request, "create_car.html, context")
        
def register_user(request):
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

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_json(request):
    products_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in products_list
    ]

    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) # strip HTML tags!
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name, 
        description=description,
        price=price,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_entry_ajax(request, id):
    try:
        product = Product.objects.get(pk=id, user=request.user)

        product.name = strip_tags(request.POST.get("name"))
        product.description = strip_tags(request.POST.get("description"))
        product.price = request.POST.get("price")
        product.category = request.POST.get("category")
        product.thumbnail = request.POST.get("thumbnail")
        product.is_featured = request.POST.get("is_featured") == 'on'
        product.save()

        return HttpResponse(b"UPDATED", status=200)
    except Product.DoesNotExist:
        return HttpResponse(b"NOT FOUND", status=404)
    
@require_POST
def login_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        update_last_login(None, user)
        return JsonResponse({'status': 'success', 'message': 'Login berhasil', 'redirect_url': reverse('main:show_main')})

    else:
        return JsonResponse({'status': 'error', 'message': 'Username atau password salah'}, status=400)

@require_POST
def register_ajax(request):
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if not username or not password1 or not password2:
        return JsonResponse({'status': 'error', 'message': 'Username dan password wajib diisi'}, status=400)

    if password1 != password2:
        return JsonResponse({'status': 'error', 'message': 'Password tidak sama'}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({'status': 'error', 'message': 'Username sudah dipakai'}, status=400)

    User.objects.create_user(username=username, password=password1)
    return JsonResponse({'status': 'success', 'message': 'Registrasi berhasil', 'redirect_url': reverse('main:login')})
