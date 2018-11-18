from django.urls import path
from . import views

urlpatterns = [
    path('', views.KirjoitusListView.as_view(), name='koti'),
    path('kirjoitus/<int:pk>', views.KirjoitusDetailView.as_view(), name='yksityiskohdat'),
    path('kirjoitus/uusi/', views.KirjoitusCreateView.as_view(), name='uusi_kirjoitus'),
    path('kirjoitus/<int:pk>/muokkaa/', views.KirjoitusUpdateView.as_view(), name='muokkaa'),
    path('kirjoitus/<int:pk>/poista/', views.KirjoitusDeleteView.as_view(), name='poista'),


]
