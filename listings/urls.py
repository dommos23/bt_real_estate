from django.urls import path #, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="listings"),
    path('<int:listing_id>', views.listing, name="listing"),
    path('search', views.search, name="search"),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

