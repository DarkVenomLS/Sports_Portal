from django.shortcuts import get_object_or_404, render
from .models import SubEvent, MainEvent, Gallery, SportEvent
from django.views.generic import ListView, DetailView
# Create your views here.

class MainEventListView(ListView):
    model = MainEvent
    template_name = 'main_event_list.html'
    context_object_name = 'main_events'

class SubEventListView(DetailView):
    model = MainEvent
    template_name = 'sub_event_list.html'
    context_object_name = 'main_event'

class SubEventDetailsView(DetailView):
    model = SubEvent
    template_name = "sub_event_detail.html"
    context_object_name = "sub_event"

def GalleryDetailView(request, sub_event_id=None):
    if sub_event_id:
        sub_event = get_object_or_404(SubEvent, id=sub_event_id)
        images = Gallery.objects.filter(sub_event=sub_event)  # Filter images for this event
    else:
        sub_event = None
        images = Gallery.objects.all()  # Show all images if no event is selected

    sub_events = SubEvent.objects.all()  # Get all sub-events for navigation

    return render(request, 'gallery.html', {
        'sub_event': sub_event,
        'images': images,
        'sub_events': sub_events
    })

class SportsListView(ListView):
    model = SportEvent
    template_name = 'sports.html'
    context_object_name = 'sports'