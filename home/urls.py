from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('events/', views.events, name="events"),
    path('sports/', views.sports, name="sports"),
    path('teams/', views.teams, name="teams"),
    path('registration/', views.registration, name="registration"),
]
