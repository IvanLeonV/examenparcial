from django.shortcuts import render   
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import personas


   
# Create your views here.


def Vprincipal(request):
    personasTotales=personas.objects.all()
    return render(request,'Vprincipal.html',{
        'personasTotales':personasTotales
    })    
    



def Ntarea(request):
    if request.method =='POST':
        print(request.POST)
        nombre=request.POST.get('nombre')        
        fechafin=request.POST.get('fechafin')
        estado=request.POST.get('estado')
        responsable=request.POST.get('responsable')
        personas.objects.create(
            nombre=nombre,
            fecha=fechafin,
            estado='EN PROGRESO',
            responsable=responsable

        )
       # nombre=request.POST.get('nombre')
    
       
        return HttpResponseRedirect(reverse('tareasApp:Vprincipal'))
        
    return render(request,'Ntarea.html')