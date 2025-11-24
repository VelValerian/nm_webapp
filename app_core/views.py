from django.shortcuts import render

from django.shortcuts import render

def home(request):       return render(request, "pages/main.html")
def about(request):      return render(request, "pages/about.html")
def corporate(request):  return render(request, "pages/corporate.html")
def contacts(request):   return render(request, "pages/contacts.html")
