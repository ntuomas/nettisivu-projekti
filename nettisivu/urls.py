
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tilit/', include('django.contrib.auth.urls')), #django etsii automaattisesti login-sivua
    path('tilit/', include('tilit.urls')), 
    path('', include('kirjoitukset.urls')),


]
