from django.shortcuts import render
from .forms import RegistrationForm
from .models import Registration


# Create your views here.
def index(request):
    return render(request, "index.html")

def events(request):

    params = {"eventlist":["a", "b", "c"], "age": 22}
    return render(request, "events.html", params)

def sports(request):
    return render(request, "sports.html")

def teams(request):
    
    return render(request, "teams.html")

def registration(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            name = form.cleaned_data['fullname']
            college = form.cleaned_data['college']
            year_of_study = form.cleaned_data['year_of_study']
            email = form.cleaned_data['email']
            contact_number = form.cleaned_data['contact_number']
            emergency_contact = form.cleaned_data['emergency_contact']

            participant = Registration.objects.create(fullname=name, college=college, year_of_study=year_of_study, email=email, contact_number=contact_number, emergency_contact=emergency_contact)
            participant.save()
            
            return render(request,'success.html')
    form = RegistrationForm()
    return render(request, "registration.html", {'form': form})
    # return render(request, "registration.html")

def highlights(request):
    return render(request, "highlights.html")

def organisers(request):
    return render(request, "organisers.html")