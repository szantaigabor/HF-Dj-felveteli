from re import template
from django.shortcuts import render

from .models import SajatUser
#from .models import Kerdes

# Create your views here.

def index(request):
    print(request.POST)

    if request.method=="POST":
        idje = request.POST['diak_azonos']
        #print(request.POST['nev'])

        lista = list(SajatUser.objects.filter(azonosito=idje))
        print(lista)
        talalat = lista[0]
        
    template ="index.html"
    context={}
    return render(request, template, context)
        #Kerdes.objects.create(kerdes=kerdesnev)


    template= "index.html"
    context={'userneve': lista[0].nev, 'userpont':lista[0].pontszam}
    return render(request,template, context)