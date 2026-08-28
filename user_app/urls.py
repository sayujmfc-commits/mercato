from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns=[
    path('',views.home),
    path('index',views.index,name="index"),
    path('user_register',views.user_register),
    path('login',views.login),
    path('product_list',views.product_list,name="product_list"),
    path('buy_product/<int:product_id>',views.buy_product,name="buy_product")
]

