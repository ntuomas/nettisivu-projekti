from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Kirjoitus

class KirjoitusListView(ListView):
    model = Kirjoitus
    template_name = 'koti.html'

class KirjoitusDetailView(DetailView):
    model = Kirjoitus
    template_name = "yksityiskohdat.html"
    context_object_name = 'kaikkikirjoitukset' #korvataan object_list

class KirjoitusCreateView(CreateView):
    model = Kirjoitus
    template_name = "uusi_kirjoitus.html"
    fields = '__all__' #kaikki kentät tietokannasta

class KirjoitusUpdateView(UpdateView):
    model = Kirjoitus
    template_name = "muokkaa.html"
    fields = ['otsikko', 'teksti']

class KirjoitusDeleteView(DeleteView):
    model = Kirjoitus
    template_name = "poista.html"
    context_object_name = 'kaikkikirjoitukset'
    success_url = reverse_lazy('koti')
