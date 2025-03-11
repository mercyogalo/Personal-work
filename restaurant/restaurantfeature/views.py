from django.shortcuts import render
from . models import Category, Product, Special, Testimonial

# Create your views here.
def home(request):
    category_items=Category.objects.all()
    testimonials=Testimonial.objects.all()
    specials=Special.objects.all()
    context={
        "category_items":category_items,
        "testimonials":testimonials,
        "specials":specials,
    }
    
    return render(request,'index.html', context)


def menu(request):
    return render(request,'menu.html')

def reservation(request):
    return render(request,'reservation.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')