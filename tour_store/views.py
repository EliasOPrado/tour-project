from django.shortcuts import render, get_object_or_404
from .models import Destinations

# Create your views here.
def main_view(request):
    return render(request, 'main.html')

def destinations(request):
    destinations = Destinations.objects.all()
    return render(request, 'destinations.html', {'destinations': destinations})

def destination_details(request, id):
    # Get a singular destination, or return a 404
    details= get_object_or_404(Destinations, pk=id)
    return render(request, 'details.html', {'details':details})
