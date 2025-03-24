from django.contrib import admin
from .models import MainEvent, SubEvent, Gallery, SportEvent
# Register your models here.

admin.site.register(SportEvent)
admin.site.register(MainEvent)
admin.site.register(SubEvent)
admin.site.register(Gallery)