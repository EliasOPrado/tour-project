from django.shortcuts import render, redirect, reverse
from tour_store.models import Destinations
from django.contrib.auth.decorators import login_required
# Create your views here.

def view_cart(request):
    """A view that renders the cart contents page """
    cart = request.session.get('cart', {})
    # if trying to open cart page this view without a product in cart
    # this view will redirect to destination
    if not cart:
        return redirect(reverse('destination'))
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    #Gets the name='quantity' from input form
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount

    url for this function should be <str:id> not <int:id>
    - otherwise you need to add str() method for each dict representation.
    """
    cart = request.session.get('cart', {})
    quantity = cart[id] - 1 # decreases the cart quantity until deletes from cart

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    if not cart: #if all products be deleted from cart return to destination page
        return redirect(reverse('destination'))
    return redirect(reverse('view_cart'))
