from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about us.html')

def gallary(request):
    return render(request,'gallary.html')

def contacts (request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')