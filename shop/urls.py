from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='/'),
    path('products/', views.Products, name='products'),
    path('products/<int:id>/', views.Details, name='details'),
    # path('add_to_cart/', views.AddToCart, name='add_to_cart'),
    # path('cart/', views.Cart, name='cart'),
]