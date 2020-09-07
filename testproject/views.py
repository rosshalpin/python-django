from django.http import HttpResponse
from django.shortcuts import render
from .models import Examples

def index(request):
    return HttpResponse("Hello, world.")

def show(request):
    examp = Examples.objects.all()
    return render(request, "show.html", {'examp':examp})
