from django.shortcuts import render

def index(request):
    return render(request,"miBlog/index.html")


# Create your views here.
