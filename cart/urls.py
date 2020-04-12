from django.urls import path
from . import views

urlpatterns = [
    path('view-cart', views.view_cart, name="view_cart"),
    path('add/<int:id>/', views.add_to_cart, name="add_to_cart"),
    #items from dictionary should be used <str:id-from-dictionary>
    path('adjust/<str:id>/', views.adjust_cart, name="adjust_cart"),
]
