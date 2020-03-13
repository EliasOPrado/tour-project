from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Destinations

# Create your views here.
def main_view(request):
    return render(request, 'main.html')


def destinations(request):
    """
    This function should run the pagination
    """
    destination = Destinations.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(destination, 1)
    try:
        destinations = paginator.page(page)

    except PageNotAnInteger:
        destinations = paginator.page(1)

    except EmptyPage:
        destinations = paginator.page(paginator.num_pages)

    return render(request, 'destinations.html', {'destinations': destinations})

def destination_details(request, id):
    # Get a singular destination, or return a 404
    details= get_object_or_404(Destinations, pk=id)

    return render(request, 'details.html', {'details':details})
