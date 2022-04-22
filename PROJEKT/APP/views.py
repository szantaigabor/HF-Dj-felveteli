from re import template
from django.shortcuts import render
#from .models import Kerdes

# Create your views here.

def index(request):
    print(request.POST)

    if request.method=="POST":
        kerdesnev = request.POST['kedvencszo']
        #Kerdes.objects.create(kerdes=kerdesnev)
    template= "index.html"
    context={}#{'kerdesek': Kerdes.objects.all()}
    return render(request,template, context)