
from django.urls import path
from .views import SubEventListView, MainEventListView, SubEventDetailsView, GalleryDetailView, SportsListView


urlpatterns = [

    path('', MainEventListView.as_view(), name="main_event_list"),
    path('main-event/<int:pk>/', SubEventListView.as_view(), name='sub_event_list'),
    path('sub-event/<int:pk>/', SubEventDetailsView.as_view(), name='sub_event_detail'),
    path('sports/', SportsListView.as_view(), name='sports'),
    path('gallery/', GalleryDetailView, name="gallery"),
    path('gallery/<int:sub_event_id>/', GalleryDetailView, name="gallery_by_event"),
    
    # path('sports/', views.sports, name="sports"),
]
