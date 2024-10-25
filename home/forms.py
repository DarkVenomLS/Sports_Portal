from django import forms

class RegistrationForm(forms.Form):
    
    fullname = forms.CharField(label="Full Name", max_length=50)
    college = forms.CharField(label="College Name", max_length=100)
    year_of_study = forms.CharField(label="Year of Study",initial='BE', max_length=10)
    email = forms.EmailField(label="Email", max_length=50)
    contact_number = forms.CharField(label="Contact Number", max_length=10)
    emergency_contact = forms.CharField(label="Emergency Contact Number", max_length=10)

class TeamRegistrationForm(forms.Form):
    team_name = forms.CharField(label="Team Name", max_length=50)
    player_name = forms.CharField(label="Player Name", max_length=50)
    email = forms.EmailField(label="Email", max_length=50)
    contact_number = forms.CharField(label="Contact number", max_length=10)