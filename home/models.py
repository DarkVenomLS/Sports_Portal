from django.db import models


class Registration(models.Model):

    SPORT_CHOICES = [
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('volleyball', 'Volleyball'),
        ('kabaddi', 'Kabaddi'),
        # Add more options as needed
    ]

    fullname = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    contact_number = models.CharField(max_length=10)
    emergency_contact = models.CharField(max_length=10)
    sport = models.CharField(max_length=50, choices=SPORT_CHOICES, default='')

    def __str__(self):
        # return self.fullname, self.college, self.year_of_study, self.email, self.contact_number, self.emergency_contact
        return f"{self.fullname} | {self.email} | {self.contact_number}"
    

class TeamRegistration(models.Model):
    teamname = models.CharField(max_length=50)
    playername = models.CharField(max_length=50)
    year_of_study = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        # return self.fullname, self.college, self.year_of_study, self.email, self.contact_number, self.emergency_contact
        return f"{self.teamname.capitalize()}"












# Create your models here.
# class Sport(models.Model):
#     SPORT_TYPES = [
#         ('Cricket', 'Cricket'),
#         ('Badminton', 'Badminton'),
#         ('Football', 'Football'),
#         ('Basketball', 'Basketball'),
#         ('Table Tennis', 'Table Tennis'),
#     ]
    
#     name = models.CharField(max_length=100, choices=SPORT_TYPES)
#     def __str__(self):
#         return self.name

# class Registration(models.Model):
#     full_name = models.CharField(max_length=100)
#     #student_id = models.CharField(max_length=50)
#     college = models.CharField(max_length=50)
#     year_of_study = models.CharField(max_length=10)
#     email = models.EmailField()
#     contact_number = models.CharField(max_length=15)
#     emergency_contact = models.CharField(max_length=15)
#     sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
#     t_shirt_size = models.CharField(max_length=5, null=True, blank=True)
#     is_team_sport = models.BooleanField(default=False)

# class TeamMember(models.Model):
#     registration = models.ForeignKey(Registration, related_name='team_members', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     contact_number = models.CharField(max_length=15)
