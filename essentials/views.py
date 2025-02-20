from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import random
from .forms import CheckoutForm


def home(request):
    all_products = list(Product.objects.all())
    random.shuffle(all_products)  # Shuffle the products randomly
    latest_products = all_products[:4]
    return render(request, 'essentials/home.html' , {'latest_products': latest_products})

def about(request):
    return render(request, 'essentials/about.html')

def contact(request):
    return render(request, 'essentials/contact.html')

def mobile_accessories(request):
    products = Product.objects.filter(category='Mobile Accessories')
    return render(request, 'essentials/mobile_accessories.html', {'mobile_products': products})

def computer_accessories(request):
    products = Product.objects.filter(category='Computer Accessories')
    return render(request, 'essentials/computer_accessories.html', {'computer_products': products})

def cart(request):
    return render(request, 'essentials/cart.html')

def checkout(request):
    return render(request, 'essentials/checkout.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'essentials/product_detail.html', {'product': product})

def cart(request):
    return render(request, 'essentials/cart.html')

def update_cart_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        quantity = int(data.get('quantity'))  # Ensure quantity is an integer
        
        # Example logic to update the cart
        cart = request.session.get('cart', {})
        if title in cart:
            cart[title]['quantity'] = quantity
            request.session['cart'] = cart  # Save the updated cart back to the session
            request.session.modified = True  # Ensure the session is saved
        
        return JsonResponse({'cart': cart})
    return JsonResponse({'error': 'Invalid request'}, status=400)
import uuid
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cart

@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_title = data.get("title")
        product_price = float(data.get("price"))

        if not request.session.session_key:
            request.session.create()

        session_id = request.session.session_key

        cart_item, created = Cart.objects.get_or_create(
            session_id=session_id,
            product_title=product_title,
            defaults={"product_price": product_price, "quantity": 1},
        )

        if not created:
            cart_item.quantity += 1
            cart_item.product_price = cart_item.quantity * product_price  # Update price based on quantity
            cart_item.save()

        # Fetch updated cart
        cart_items = Cart.objects.filter(session_id=session_id).values("product_title", "product_price", "quantity")

        return JsonResponse({"message": "Added to cart", "cart": list(cart_items)})



def get_cart(request):
    if not request.session.session_key:
        return JsonResponse({"cart": []})

    session_id = request.session.session_key
    cart_items = Cart.objects.filter(session_id=session_id).values("product_title", "product_price", "quantity")

    return JsonResponse({"cart": list(cart_items)})


@csrf_exempt
def remove_from_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_title = data.get("title")

        if not request.session.session_key:
            return JsonResponse({"message": "No active session"}, status=400)

        session_id = request.session.session_key

        cart_item = get_object_or_404(Cart, session_id=session_id, product_title=product_title)

        unit_price = cart_item.product_price / cart_item.quantity  # Calculate price of one unit

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.product_price = cart_item.quantity * unit_price  # Update price based on new quantity
            cart_item.save()
        else:
            cart_item.delete()

        # Fetch updated cart
        cart_items = Cart.objects.filter(session_id=session_id).values("product_title", "product_price", "quantity")

        return JsonResponse({"message": "Item removed", "cart": list(cart_items)})




def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Save the order
            order = form.save(commit=False)
            order.save()

            # Clear the cart after checkout
            session_id = request.session.session_key
            Cart.objects.filter(session_id=session_id).delete()

            messages.success(request, f"Order {order.order_number} has been placed successfully!")
            return redirect('order_confirmation', order_number=order.order_number)
    else:
        form = CheckoutForm()

    # Calculate the total price for each item in the cart
    cart = Cart.objects.filter(session_id=request.session.session_key)
    for item in cart:
        item.total_price = item.product_price * item.quantity

    total_amount = sum(item.total_price for item in cart)

    return render(request, 'essentials/checkout.html', {
        'form': form,
        'cart': cart,
        'total_amount': total_amount
    })

def order_confirmation(request, order_number):
    order = Order.objects.get(order_number=order_number)
    return render(request, 'essentials/order_confirmation.html', {'order': order})