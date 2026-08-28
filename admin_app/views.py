def add_product(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            quantity=quantity,
            image=image
        )

        return redirect('add_product')

    return render(request, 'add_product.html')

from django.shortcuts import render, redirect
from .models import Product


def add_product(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            quantity=quantity,
            image=image
        )

        return redirect('add_product')

    return render(request, 'add_product.html')


def logout(request):

    session_key = list(request.session.keys())

    for key in session_key:
        del request.session[key]

    return redirect('index')