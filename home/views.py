from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def events(request):
    return render(request, "events.html")

def sports(request):
    return render(request, "sports.html")

def teams(request):
    return render(request, "teams.html")

def highlights(request):
    return render(request, "highlights.html")

def organisers(request):
    return render(request, "organisers.html")

def registration(request):
    return render(request, "registration.html")