from django.shortcuts import render, redirect
from . models import Category, Product, Special, Testimonial
from django.contrib import messages

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
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        date=request.POST['date']
        time=request.POST['time']
        people=request.POST['people']
        
        messages.success(request, ("You reservation has been made succcessfully. Check your email for the details."))
        return redirect('restaurantfeature:reservation')
    else: 
        return render(request,'reservation.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')