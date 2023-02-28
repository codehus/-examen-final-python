from django.shortcuts import render
from django.http import HttpResponse
from .models import Platos
# Create your views here.
def platillos_list(request):
    # name = 'Estos son los platos'
    # return HttpResponse(name)

    # p = Platos(nombre='Cau cau',precio=50,procedencia='Perú')
    # p.save()

    #platillos = Platos.objects.all()
    platillos = Platos.objects.filter(procedencia='Perú',precio__gte=40)
    return render(request, 'platos/platos_list.html', context={'data': platillos})