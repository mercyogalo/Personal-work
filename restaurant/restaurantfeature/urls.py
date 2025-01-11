from django.urls import path
from . import views

app_name = "restaurantfeature"

urlpatterns = [
    path("", views.home, name="home"),  
]