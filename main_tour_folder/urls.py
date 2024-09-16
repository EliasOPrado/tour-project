"""main_tour_folder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from tour_store import views

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

admin.site.site_header = "Tour Project admin"
admin.site.site_title = "Tour Project admin"
admin.site.index_title = "Tour Project admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main_view, name="index"),
    # Include tour_store apps
    path("accounts/", include("accounts.urls")),  # account reset url
    path("store/", include("tour_store.urls")),
    path("cart/", include("cart.urls")),
    path("search/", include("search.urls")),
    path("chekout/", include("checkout.urls")),
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
