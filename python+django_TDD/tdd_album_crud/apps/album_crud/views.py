from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, "index.html")

def add(request):
    if request.method == "POST":
        Album.objects.create(title = request.POST["title"], artist = request.POST["artist"], year = request.POST["year"])
    return redirect('/')

def delete(request):
    return redirect('/')

def edit(request, id):
    context = {
        "album" : Album.objects.get(id = id)
    }
    return render(request, "index.html", context)