
from django.urls import include, path
from .views import ParticipantCreateView, ParticipantListView, download_participants_excel, success_page

urlpatterns = [
    # path('', ParticipantCreateView.as_view(), name='registration'),
    path('sub-event/<int:sub_event_id>/register/', ParticipantCreateView.as_view(), name='participant_register'),
    path('view-participants/', ParticipantListView.as_view(), name="view-participants"),
    path('download-excel/', download_participants_excel, name="download_participants_excel"),
    path('success/', success_page, name="success_page")
]
