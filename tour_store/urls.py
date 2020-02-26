from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.destinations, name="destination"),
    path('destination-details/<int:id>/', views.destination_details, name="destinationDetails")
]
