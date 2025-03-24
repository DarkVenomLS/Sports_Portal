# Create your views here.
from django.http import HttpResponse
import openpyxl
from django.shortcuts import get_object_or_404, render, redirect
# from django.views.generic import CreateView
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .models import Participant, Registration, TeamRegistration
from events.models import SubEvent
from .forms import RegistrationForm, TeamRegistrationForm, PlayerFormSet  # Ensure this form exists


# class ParticipantCreateView(CreateView):
#     model = Participant
#     fields = ['full_name', 'email', 'contact_number', 'sub_event', 'college_name']
#     success_url = 'events/'  # Redirect to main event list after registration

class ParticipantListView(ListView):
    model = Participant
    template_name = "view-participants.html"
    context_object_name = "view_participants"

class ParticipantCreateView(View):
    template_name = 'participant_register.html'
    
    def get(self, request, sub_event_id):
        sub_event = get_object_or_404(SubEvent, id=sub_event_id)  # Fetch the sub-event
        form = RegistrationForm(initial={'sub_event': sub_event})  # Pre-fill sub-event
        return render(request, self.template_name, {'form': form, 'sub_event': sub_event})
    
    def post(self, request, sub_event_id):
        sub_event = get_object_or_404(SubEvent, id=sub_event_id)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.sub_event = sub_event  # Ensure the correct sub-event is saved
            participant.save()
            return render(request, 'success.html')  # Redirect after successful registration
        return render(request, self.template_name, {'form': form, 'sub_event': sub_event})


def download_participants_excel(request):
    # Create an Excel workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Participants"

    # Define column headers
    headers = ["Name", "College Name", "Year of Study", "Contact", "Emergency Contact"]
    sheet.append(headers)  # Add headers to the first row

    # Fetch participant data and write to Excel rows
    participants = Participant.objects.all()
    for participant in participants:
        sheet.append([
            participant.full_name,
            participant.college_name,
            participant.year_of_study,
            participant.contact_number,
            participant.emergency_contact
        ])

    # Prepare the HTTP response
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="participants.xlsx"'

    # Save the workbook to the response
    workbook.save(response)
    return response



# def register_participant(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # Redirect to success page
#     else:
#         form = RegistrationForm()
    
#     return render(request, 'registration.html', {'form': form})

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
            # return render(request,'success.html')
            return redirect('teamRegistration')
    form = RegistrationForm()
    return render(request, "templates/registration.html", {'form': form})

def success_page(request):
    return render(request, 'success.html')

def teamRegistration(request):
    if (request.method == 'POST'):
        form = TeamRegistrationForm(request.POST)
        player_formset = PlayerFormSet(request.POST)

        if (form.is_valid() and player_formset.is_valid()):
             # Extract data manually from the form
            teamname = form.cleaned_data['teamname']
            # team = TeamRegistration.objects.create(teamname=teamname)
            # team = form.save()

            # teamname = form.cleaned_data['teamname']
            for player_form in player_formset:
                if player_form.cleaned_data:
                    playername = form.cleaned_data['playername']
                    year_of_study = form.cleaned_data['year_of_study']
                    contact_number = form.cleaned_data['contact_number']

                    player = TeamRegistration.objects.create(teamname=teamname, playername=playername, year_of_study=year_of_study, contact_number=contact_number)
                    player.save()
            return render(request,'success.html')
    form = TeamRegistrationForm()
    player_formset = PlayerFormSet()
    return render(request, "register_team.html", {'form': form, 'player_formset': player_formset})

