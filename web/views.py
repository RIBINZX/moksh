from django.shortcuts import render
from .models import Service,Gallery,Package
# Create your views here.

def index(request):
    gallery=Gallery.objects.all()
    context = {'gallery':gallery}
    return render(request, "web/index.html", context)


def about(request):
    context = {}
    return render(request, "web/about.html", context)

def contact(request):
    context = {}
    return render(request, "web/contact.html", context)

def delux(request):
    context = {}
    return render(request, "web/deluxe.html", context)


def restaurant(request):
    package=Package.objects.all()
    context = {'package':package}
    return render(request, "web/restaurant.html", context)


def Services(request):
    service=Service.objects.all()
    context = {"service":service}
    return render(request, "web/Services.html", context)

def gallery(request):
    gallery=Gallery.objects.all()
    context = {'gallery':gallery}
    return render(request, "web/gallery.html", context)
