from django.db import models

# Create your models here.
class Registration(models.Model):

    fullname = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    contact_number = models.CharField(max_length=10)
    emergency_contact = models.CharField(max_length=10)

    def __str__(self):
        # return self.fullname, self.college, self.year_of_study, self.email, self.contact_number, self.emergency_contact
        return f"{self.fullname} | {self.email} | {self.contact_number}"

class TeamRegistration(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=50)
    player_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact_number = models.CharField(max_length=10)