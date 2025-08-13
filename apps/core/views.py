from django.shortcuts import render

def HomeView(request):
    return render (request , "core/index.html")

def AboutView(request):
    return render (request , "core/about.html")

def ContactView(request):
    return render(request , "core/contact.html")