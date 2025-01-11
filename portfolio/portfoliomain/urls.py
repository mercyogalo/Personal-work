from django.urls import path

app="portfoliofeatures"

urlpatterns = [
    path("/", views.home, name="home"),
    path("about/", views.about, name="about"),
 
]