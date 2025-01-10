
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("resume/", views.resume, name="resume"),
]