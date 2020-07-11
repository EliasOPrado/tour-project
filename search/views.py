from django.shortcuts import render
from tour_store.models import Destinations
# Create your views here.

def do_search(request):
    """Search a retreat by its title"""
    if request.method == "GET":
        # 'q' is the name in the form that will be get// "tour_title" (from Destinations model tag) is the name that will be searched
        destinations = Destinations.objects.filter(location__icontains=request.GET['q'])
        return render(request, 'destinations.html', {'destinations': destinations})
