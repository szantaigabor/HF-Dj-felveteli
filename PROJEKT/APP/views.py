from re import template
from django.shortcuts import render

from PROJEKT.APP.models import SajatUser
#from .models import Kerdes

# Create your views here.

def index(request):
    print(request.POST)

    if request.method=="POST":
        idje = request.POST['diak_azonos']

        lista = list(SajatUser.objects.filter(azonosito=idje))
        #Kerdes.objects.create(kerdes=kerdesnev)


    template= "index.html"
    context={}#{'kerdesek': Kerdes.objects.all()}
    return render(request,template, context)