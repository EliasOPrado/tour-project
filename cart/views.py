from django.shortcuts import render, redirect, reverse
from tour_store.models import Destinations
# Create your views here.

def view_cart(request):
    """A view that renders the cart contents page """

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

# def remove_from_cart(request, id):
#     """ Remove an item from the cart """
#     print(cart)
#     cart = request.session.get('cart', {})
#     quantity = request.POST.get('quantity')
#     cart.pop(id, quantity) # Then pop the item out of it
#     return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount

    url for this function should be <str:id> not <int:id>
    """

    cart = request.session.get('cart', {})
    quantity = cart[id] - 1 #decreases the cart quantity until deletes from cart

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    if cart == {}:
        return redirect(reverse('destination'))
    return redirect(reverse('view_cart'))
