from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from .models import ipGenerate
from .forms import GeneralForms



# Create your views here.
class GeneraList(ListView):
    model = ipGenerate
    paginate_by = 5

class GenerarIp(CreateView):
    model = ipGenerate
    form_class = GeneralForms
    success_url = reverse_lazy('home') 
    # success_url = reverse_lazy('home')

class GeneraUp(UpdateView):
    model = ipGenerate
    forms_class = GeneralForms
    
    def get_success_url(self):
        success_url = reverse_lazy('home')
        return success_url

class GeneraDel(DeleteView):
    model = ipGenerate
    success_url = reverse_lazy('home')
    

    
    




    