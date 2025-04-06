from django.shortcuts import render, redirect
from . models import Category, Product, Special, Testimonial, Chef, Gallery
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage

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
    products=Product.objects.all()
    
    context={
        "products":products
    }
    return render(request,'menu.html',context)

def reservation(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        date=request.POST['date']
        time=request.POST['time']
        people=request.POST['people']
        
        
        reserver_subject='Reservation Confirmation Details'
        reserver_message= f"""
              <html>
        <body style="background-color: #BB9F5E; font-family: Arial, sans-serif; color: #333;">
            <div style="background-color: #BB9F5E; padding: 20px; text-align: center;">
                <h3 style="color: white;">Reservation Confirmation  for table number  12A</h3>
                
                <p style="color: white;">Dear {name},</p>
                
                <p style="color: white;">
                Thank you for making your reservation with us.
                </p>
                
                <table border="1" cellpadding="10" cellspacing="0" style="width: 80%; margin: 0 auto; border-collapse: collapse; background-color: white;">
                    <tr>
                        <th style="background-color: #BB9F5E; color: white; text-align: left; padding: 10px;">Name</th>
                        <td style="text-align: left; padding: 10px;">{name}</td>
                    </tr>
                    <tr>
                        <th style="background-color: #BB9F5E; color: white; text-align: left; padding: 10px;">Email</th>
                        <td style="text-align: left; padding: 10px;">{email}</td>
                    </tr>
                    <tr>
                        <th style="background-color: #BB9F5E; color: white; text-align: left; padding: 10px;">Phone</th>
                        <td style="text-align: left; padding: 10px;">{phone}</td>
                    </tr>
                    <tr>
                        <th style="background-color: #BB9F5E; color: white; text-align: left; padding: 10px;">Date</th>
                        <td style="text-align: left; padding: 10px;">{date}</td>
                    </tr>
                    <tr>
                        <th style="background-color: #BB9F5E; color: white; text-align: left; padding: 10px;">Time</th>
                        <td style="text-align: left; padding: 10px;">{time}</td>
                    </tr>
                    <tr>
                        <th style="background-color: #BB9F5E; color: white; text-align: left; padding: 10px;">People</th>
                        <td style="text-align: left; padding: 10px;">{people}</td>
                    </tr>
                </table>
                <p style="color: white;">We look forward to hosting you soon!</p>
                <p style="color: white;">Best regards,<br>Restaurantly.com</p>
            </div>
        </body>
        </html>
        """
        
        
        email=EmailMessage(
            reserver_subject, #subject
            reserver_message,
             'ogalomercy8@gmail.com', # from
            [email], #to
        )
        email.content_subtype='html' 
        email.send(fail_silently=False)

        
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
        hr_message=f'Name:{name} \n   Email:{email}    \n   Message:{message}'
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
                "Best regards,\n Restaurantly.com\n\n"
                 "If you have any questions, feel free to reply to this email.\n"
                    "Restaurantly Team\n\n"
                    "If this message ends up in your spam folder, please mark it as 'Not Spam' to ensure future communication."
        )
        sender_subject=f'Thank you for reaching out' 
        
        send_mail(
            sender_subject,
            sender_message,
            'ogalomercy8@gmail.com',#from email
            [email],#to email
            fail_silently=False
        )
        
        messages.success(request,("Your message has been received successfully. Our team will get back to you shortly"))
        return redirect('restaurantfeature:contact')
    else:
        return render(request,'contact.html')

def about(request):
    chefs=Chef.objects.all()
    gallerys=Gallery.objects.all()
    
    context={
        'chefs':chefs,
        'gallerys':gallerys
    }
    return render(request,'about.html')