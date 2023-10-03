from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
cart = []
cart_value = 99

def Home(request):
    return render(request, 'home.html', {'cart_value': cart_value})

def Products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'cart_value': cart_value})

def Details(request, id):
    details = get_object_or_404(Product, pk=id)
    return render(request, 'details.html', {'details': details, 'cart_value': cart_value})

# def AddToCart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         if product_id:
#             product = get_object_or_404(Product, pk=product_id)

#             if 'cart' not in request.session:
#                 request.session['cart'] = []
#             cart = request.session['cart']

#             for item in cart:
#                 if item['product_id'] == product.id:
#                     item['quantity'] += 1
#                     break

#             else:
#                 request.session['cart'].append({'product_id': product.id, 'quantity': 1})
                
#             request.session.modified = True

#     return redirect('products')

# def Cart(request):
#     total_price = 0
#     if 'cart' in request.session:
#         for item in request.session['cart']:
#             product = Product.objects.get(pk=item['product_id'])
#             subtotal = product.price * item['quantity']
#             total_price += subtotal
#             cart.append({
#                 'product': product,
#                 'quantity': item['quantity'],
#                 'subtotal': subtotal,
#             })
#     return render(request, 'cart.html', {'cart': cart, 'total_price': total_price, 'cart_value': cart_value})
    


