from django.shortcuts import render
from .models import Destinations

# Create your views here.
def main_view(request):
    return render(request, 'main.html')

def destinations(request):
    destinations = Destinations.objects.all()
    return render(request, 'destinations.html', {'destinations': destinations})
