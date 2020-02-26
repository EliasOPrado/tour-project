from django.shortcuts import render
from .models import tour_destinations

# Create your views here.
def main_view(request):
    return render(request, 'main.html')

def destinations(request):
    destinations = tour_destinations.objects.get(id=pk)
    return render(request, 'destinations.html', {'destinations': destinations})
