# from django import forms 
# from django.forms import formset_factory

# class RegistrationForm(forms.Form):
#     # choices = ['Cricket', 'Football', 'Voleyball', 'Kabaddi']
#     fields = ['fullname','college', 'year_of_study', 'email', 'contact_number', 'emergency_contact']
#     fullname = forms.CharField(label="Full Name", max_length=50)
#     college = forms.CharField(label="College Name", max_length=100)
#     year_of_study = forms.CharField(label="Year of Study", max_length=10)
#     email = forms.EmailField(label="Email", max_length=50)
#     contact_number = forms.CharField(label="Contact Number", max_length=10)
#     emergency_contact = forms.CharField(label="Emergency Contact Number", max_length=10)
#     SPORT_CHOICES = [
#         ('', 'Select a sport'),  # Placeholder option
#         ('cricket', 'Cricket'),
#         ('football', 'Football'),
#         ('volleyball', 'Volleyball'),
#         ('kabaddi', 'Kabaddi'),
#         # Add more sports as needed
#     ]
#     sport = forms.ChoiceField(choices=SPORT_CHOICES, required=True)
#     # sport = forms.ChoiceField(label="Sport", choices=choices)


# class TeamRegistrationForm(forms.Form):
#     # choices = ['Cricket', 'Football', 'Voleyball', 'Kabaddi']
#     # fields = ['fullname','college', 'year_of_study', 'email', 'contact_number', 'emergency_contact']
#     teamname = forms.CharField(label="Team Name", max_length=50)
#     playername = forms.CharField(label="Playe Name", max_length=50)
#     year_of_study = forms.CharField(label="Year of Study", max_length=10)
#     contact_number = forms.CharField(label="Contact Number", max_length=10)
#     # sport = forms.ChoiceField(label="Sport", choices=choices)

# PlayerFormSet = formset_factory(TeamRegistrationForm, extra=3)
