import json
from django.shortcuts import render, redirect, HttpResponse
from .models import Products, Orders
from .models import PetProfile
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here
def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Pass didn't match")
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'shop/signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        # Check if both username and password are provided
        if username and password:
            # Attempt to authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                return redirect('index')  # Redirect to home page
            else:
                # Authentication failed, show error message
                return HttpResponse("Username or Password is incorrect")

        else:
            # Username or password is missing
            return HttpResponse("Please provide both username and password")

    return render(request, 'shop/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    product_objects = Products.objects.all()
#search code
    item_name =request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = Products.objects.filter(title__icontains=item_name)

#paginator code
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request, 'shop/index.html',{'product_objects':product_objects})

# for cart
@login_required
def cart(request):
    # Assuming you have a session or a model to handle cart items
    cart_items = request.session.get('cart', {})
    return render(request, 'shop/cart.html', {'cart_items': cart_items})



def about_us(request):
    return render(request, 'shop/about_us.html')

def profile(request):
    return render(request, 'shop/profile.html')


def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html',{'product_object':product_object})





def checkout(request):
    if request.method == 'POST':
        # Variables are initialized via POST data
        items = json.loads(request.POST.get('items', '{}'))
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip = request.POST.get('zip', "")
        total=request.POST.get('total', "")

        # Create and save the order when POST data is received
        order = Orders(items=items, name=name, email=email, address=address, city=city, state=state, zip=zip,total=total)
        order.save()

        # Redirect to a success page or render a template directly
        return render(request, 'shop/checkout.html')
    else:
        # For GET and other methods, typically you show the form to fill out
        # You could also include initial data or context if necessary
        return render(request, 'shop/checkout.html')