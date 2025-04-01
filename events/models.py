from django.db import models

# Create your models here.
from datetime import time

# Create your models here.

class MainEvent(models.Model):
    name = models.CharField(max_length=100)  # Main event name
    description = models.TextField(blank=True, null=True)  # Description of the main event
    start_date = models.DateField()  # Start date of the event
    end_date = models.DateField()  # End date of the event

    def __str__(self):
        return self.name
    
class SportEvent(models.Model):
    name = models.CharField(max_length=100)  # Main event name
    description = models.TextField(blank=True, null=True)  # Description of the main event
    start_date = models.DateField()  # Start date of the event
    end_date = models.DateField()  # End date of the event

    def __str__(self):
        return self.name

class SubEvent(models.Model):
    main_event = models.ForeignKey(MainEvent, on_delete=models.CASCADE, related_name='sub_events')  # Linked to MainEvent
    dept = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=100)  # Sub-event name (e.g., Cricket, Coding Competition)
    description = models.TextField(blank=True, null=True)  # Optional description of the sub-event
    date = models.DateField()  # Date of the sub-event
    time = models.TimeField()  # Time of the sub-event
    venue = models.CharField(max_length=200)  # Venue location
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  # Venue location

    def __str__(self):
        return f"{self.name} ({self.main_event.name})"

class Sports(models.Model):
    pass

class Gallery(models.Model):
    sub_event = models.ForeignKey(SubEvent, on_delete=models.CASCADE, related_name='gallery')  # Linked to SubEvent
    image = models.ImageField(upload_to='event_photos/')  # Path to upload images
    caption = models.CharField(max_length=500, blank=True, null=True)  # Optional caption for the image

    def __str__(self):
        return f"Gallery for {self.sub_event.name}"


# # 
# # 
# # 


# # Resource model to manage different resources like equipment, venues, and personnel
# class Resource(models.Model):
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=50)  # Venue, Equipment, Personnel
#     status = models.CharField(max_length=10, default="available")
#     time_slots = models.ManyToManyField('TimeSlot', related_name="resources", blank=True)  # Link with time slots

#     def __str__(self):
#         return f"{self.name.capitalize()}"


# # TimeSlot model to manage the specific time ranges for each resource
# class TimeSlot(models.Model):
#     resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="time_slots_related")
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()

#     def __str__(self):
#         return f"{self.resource.name} ({self.start_time} - {self.end_time})"


# # Event model to manage events that require resources
# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     date = models.DateField()
#     time = models.TimeField()
#     required_resources = models.ManyToManyField(Resource, related_name="events")  # Many-to-many relation with resources

#     def __str__(self):
#         return f"{self.name.capitalize()}"


# # Allocation model to track resource allocation to specific events with time slots
# class Allocation(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
#     start_time = models.TimeField(default=time(0, 0))  # Default to midnight
#     end_time = models.TimeField(default=time(0, 0))  # Default to midnight

#     def __str__(self):
#         return f"{self.event.name.capitalize()} | {self.resource.name}"


# # Example: You can manage the available resources by creating TimeSlots.
# # Resources can then be assigned to events with start and end times.
