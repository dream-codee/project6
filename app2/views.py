from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to Index of app2</h1>")

def sample(request):
    return render(request,"sample2.html")

def sample_view(request):
    return render(request,"sample_app2.html")

# Create your views here.
