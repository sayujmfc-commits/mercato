from django.shortcuts import render
from .models import *
from admin_app.models import *


def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def user_register(request):

    if request.method == "POST":

        userphoto = request.FILES["userphoto"]
        username = request.POST.get("username")
        useremail = request.POST.get("useremail")
        userphone = request.POST.get("userphone")
        userpassword = request.POST.get("userpassword")

        data = user_details(
            userphoto=userphoto,
            username=username,
            useremail=useremail,
            userphone=userphone,
            userpassword=userpassword
        )

        data.save()

    return render(request, 'user_register.html')


def login(request):

    useremail = request.POST.get('useremail')
    userpassword = request.POST.get('userpassword')

    if useremail == 'admin@gmail.com' and userpassword == 'admin':

        request.session['useremail'] = useremail
        request.session['admin'] = 'admin'

        return render(request, 'index.html', {
            'status': 'admin login.success'
        })

    elif user_details.objects.filter(
        useremail=useremail,
        userpassword=userpassword
    ).exists():

        userdetails = user_details.objects.get(
            useremail=request.POST['useremail'],
            userpassword=userpassword
        )

        if userdetails.userpassword == request.POST['userpassword']:

            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.username
            request.session['uemail'] = useremail
            request.session['user'] = 'user'

            return render(request, 'index.html')

    else:

        return render(request, 'login.html')


def product_list(request):

    products = Product.objects.all().order_by('-id')

    return render(request, 'product_list.html', {
        'products': products
    })


def buy_product(request, product_id):

    product = Product.objects.get(id=product_id)

    # Check stock before showing delivery page
    if product.quantity <= 0:

        return render(request, 'product_list.html', {
            'products': Product.objects.all().order_by('-id'),
            'status': 'This product is currently out of stock.'
        })

    if request.method == "POST":

        customer_name = request.POST.get("customer_name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        payment_method = request.POST.get("payment_method")

        # Create the order
        Order.objects.create(
            product=product,
            customer_name=customer_name,
            phone=phone,
            address=address,
            city=city,
            pincode=pincode,
            payment_method=payment_method
        )

        # Reduce quantity by 1
        product.quantity = product.quantity - 1
        product.save()

        # Show success page
        return render(request, 'order_success.html', {

            'product': product,
            'customer_name': customer_name,
            'address': address,
            'city': city,
            'pincode': pincode,
            'payment_method': payment_method

        })

    # Show delivery address page
    return render(request, 'delivery_address.html', {
        'product': product
    })