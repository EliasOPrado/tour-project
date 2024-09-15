from django.urls import path
from . import views


urlpatterns = [path("", views.do_search, name="search")]
