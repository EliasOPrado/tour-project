from django.shortcuts import get_object_or_404
from tour_store.models import Destinations

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    destination_count = 0

    for id, quantity in cart.items():
        destination = get_object_or_404(Destinations, pk=id)
        price = destination.price
        total += quantity * destination.price
        destination_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'destination': destination, 'price':price})
    #cart_item will loop into the cart.
    return {'cart_items': cart_items, 'total': total, 'destination_count': destination_count}
