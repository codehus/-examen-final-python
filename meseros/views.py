from django.shortcuts import render
from django.http import HttpResponse
from .models import F
from .models import Meseros
# Create your views here.
def meseros_list(request):
    #name = 'Estos son nuestros meseros'
    #return HttpResponse(name)

    #meseros = Meseros.objects.all()
    #meseros = Meseros.objects.filter(pais='Perú',edad__lt=30)

    #Meseros.objects.filter(edad__ste=17).update(edad=F('edad') + 5)




    return render(request, 'meseros/meseros_list.html', context={'data': meseros})