from django.shortcuts import render, redirect
from . models import Category, Product, Special, Testimonial, Chef
from django.contrib import messages
from django.core.mail import send_mail

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
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        
        hr_subject=f'New Form Submission: {subject}'
        hr_message=f'Name:{name} \n   Email:{email}   \n \n   Message:{message}'
        hr_recipient='ogalomercy8@gmail.com'
        
        send_mail(
            hr_subject, #subject
            hr_message, #message
            email, #from email
            [hr_recipient], #to email
            fail_silently=False
        )
        
        sender_message=(
             f"Dear {name},\n\n"
                "Thank you for reaching out to us. Our HR team has received your message and will get back to you shortly.\n\n"
                "Best regards,\n Restaurantly.com"
        )
        sender_subject=f'Thank you for reaching out' 
        
        send_mail(
            sender_subject,
            sender_message,
            hr_recipient,
            [email],
            fail_silently=False
        )
        
        messages.success(request,("Your message has been received successfully. Our team will get back to you shortly"))
        return redirect('restaurantfeature:contact')
    else:
        return render(request,'contact.html')

def about(request):
    chefs=Chef.objects.all()
    
    context={
        'chefs':chefs,
    }
    return render(request,'about.html')