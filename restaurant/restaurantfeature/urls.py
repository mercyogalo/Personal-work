from django.urls import path
from . import views

app_name = "restaurantfeature"

urlpatterns = [
    path("", views.home, name="home"),  
    path("menu/", views.menu, name="menu"),
    path("reservation/", views.reservation, name="reservation"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]