from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def base(request):
    return render(request,'base.html')
def index(request):
    return render(request,'index.html')
def services(request):
    return render(request,'services.html')