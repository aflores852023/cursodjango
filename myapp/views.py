from django.http import HttpResponse
from django.shortcuts import render




# Create your views here.
def index (request):
    return render(request,"myapp/index.html")

    
# Create your views here.
def contacto (request):
    return render(request,"myapp/contacto.html")
