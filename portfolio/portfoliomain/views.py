from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def resume(request):
    return render(request, "resume.html")
