from django.shortcuts import render
from tour_store.models import Destinations
# Create your views here.

def do_search(request):
    # 'q' is the name in the form that will be get// tour_title is the name that will be searched
    destinations = Destinations.objects.filter(tour_title__icontains=request.GET['q'])
    return render(request, 'destinations.html', {'destinations': destinations})
