from django.shortcuts import render
from django.http import HttpResponse
#from .models import F
from .models import Meseros
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Meseros.forms import MeserosForm
# Create your views here.
def meseros_list(request):
    #name = 'Estos son nuestros meseros'
    #return HttpResponse(name)

    meseros = Meseros.objects.all()
    #meseros = Meseros.objects.filter(pais='Perú',edad__lt=30)

    #Meseros.objects.filter(edad__ste=17).update(edad=('edad') + 5)

    return render(request, 'meseros/meseros_list.html', context={'data': meseros})


#Vistas basadas en clases

class MeserosCreate(CreateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros/meseros-create.html'
    success_url = reverse_lazy('meseros_list_vc')

class MeserosList(ListView):
    model = Meseros
    template_name = 'meseros/meseros_list_vc.html'

class MeserosUpdate(UpdateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros/meseros_update_vc.html'
    success_url = reverse_lazy('meseros_list_vc')


class MeserosDelete(DeleteView):
    model = Meseros
    success_url = reverse_lazy('meseros_list_vc')
    template_name = 'meseros/meseros_confirm_delete.html'