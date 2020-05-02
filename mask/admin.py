from django.contrib import admin
from .models import InitialChat,RegisteredPerson,DailyUpdate

admin.site.register(InitialChat)
admin.site.register(RegisteredPerson)
admin.site.register(DailyUpdate)
# Register your models here.
