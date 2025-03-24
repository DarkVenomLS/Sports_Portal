# from django.db import models








# from django.db import models
# from django.core.exceptions import ValidationError

# class Registration(models.Model):
#     SPORT_CHOICES = [
#         ('cricket', 'Cricket'),
#         ('football', 'Football'),
#         ('volleyball', 'Volleyball'),
#         ('kabaddi', 'Kabaddi'),
#         # Add more options as needed
#     ]
#     fullname = models.CharField(max_length=50)
#     college = models.CharField(max_length=100)
#     year_of_study = models.CharField(max_length=10)
#     email = models.EmailField(max_length=50)
#     contact_number = models.CharField(max_length=10)
#     emergency_contact = models.CharField(max_length=10)
#     sport = models.CharField(max_length=50, choices=SPORT_CHOICES, default='')

#     def __str__(self):
#         # return self.fullname, self.college, self.year_of_study, self.email, self.contact_number, self.emergency_contact
#         return f"{self.fullname} | {self.email} | {self.contact_number}"
    

# ### class Team(models.Model):
# #     teamname = models.CharField(max_length=50)
# #     def __str__(self):
# #         return self.teamname
    
# class TeamRegistration(models.Model):
#     # team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
#     teamname = models.CharField(max_length=50)
#     playername = models.CharField(max_length=50)
#     year_of_study = models.CharField(max_length=10)
#     contact_number = models.CharField(max_length=10)
    
#     ### teamname = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
#     def __str__(self):
#         # return self.fullname, self.college, self.year_of_study, self.email, self.contact_number, self.emergency_contact
#         return f"{self.playername.capitalize()} ({self.teamname})"


# class EventDetails(models.Model):   
#     number = models.AutoField(primary_key=True)
#     eventname = models.CharField(max_length=50, default='', unique=True)
#     date = models.DateField()
#     time = models.TimeField()
#     # venues = ['College ground', 'Seminar Hall', 'College Campus']
#     # equipments = {
#     #     'Cricket':['Bats', 'Balls', 'Scoreboard'],
#     #     'Football':['Goal Post', 'Footballs', 'Scoreboard'],
#     #     'Volleyball':['Net', 'Voleyballs', 'Scoreboard'],
#     #     'Kabaddi':['Mat', 'Scoreboard'],
#     #     'Badminton':['Net', 'Rackets','Shuttles', 'Scoreboard'],
#     # }
#     # resources = models.CharField(max_length=30, choices=SELECT_RESOURCES, default="")
#     def __str__(self):
#         return str(self.eventname)
    

# class Resources(models.Model):
#     VENUE_CHOICES = [('college ground','College ground'), ('seminar hall','Seminar Hall'), ('college campus','College Campus')]
#     event = models.ForeignKey(EventDetails, on_delete=models.CASCADE, related_name='resources')
#     venue = models.CharField(choices=VENUE_CHOICES, max_length=50, default='College Ground')
#     # venue = models.CharField(max_length=50)
#     # equipments = models.JSONField(default=dict)
#     def clean(self):
#         # Ensure the venue is not double-booked
#         if Resources.objects.filter(
#             venue=self.venue,
#             event__date=self.event.date,
#             event__time=self.event.time
#         ).exists():
#             raise ValidationError("The venue is already booked for this date and time.")

#     def __str__(self):
#         return self.venue
    
# class Equipment(models.Model):
#     name = models.CharField(max_length=50)
#     quantity = models.PositiveIntegerField()
#     event = models.ForeignKey(EventDetails, on_delete=models.CASCADE, related_name='equipment')

#     def __str__(self):
#         return f"{self.name} ({self.quantity}) for {self.event.eventname}"




# # Create your models here.
# # class Sport(models.Model):
# #     SPORT_TYPES = [
# #         ('Cricket', 'Cricket'),
# #         ('Badminton', 'Badminton'),
# #         ('Football', 'Football'),
# #         ('Basketball', 'Basketball'),
# #         ('Table Tennis', 'Table Tennis'),
# #     ]
    
# #     name = models.CharField(max_length=100, choices=SPORT_TYPES)
# #     def __str__(self):
# #         return self.name

# # class Registration(models.Model):
# #     full_name = models.CharField(max_length=100)
# #     #student_id = models.CharField(max_length=50)
# #     college = models.CharField(max_length=50)
# #     year_of_study = models.CharField(max_length=10)
# #     email = models.EmailField()
# #     contact_number = models.CharField(max_length=15)
# #     emergency_contact = models.CharField(max_length=15)
# #     sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
# #     t_shirt_size = models.CharField(max_length=5, null=True, blank=True)
# #     is_team_sport = models.BooleanField(default=False)

# # class TeamMember(models.Model):
# #     registration = models.ForeignKey(Registration, related_name='team_members', on_delete=models.CASCADE)
# #     name = models.CharField(max_length=100)
# #     email = models.EmailField()
# #     contact_number = models.CharField(max_length=15)
