from django.shortcuts import render

# Create your views here.
def test_view(request):
    return render(request, 'index.html')
