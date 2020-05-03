from django.contrib import admin
from .models import InitialChat,RegisteredPerson,DailyUpdate,Web_Registration

admin.site.register(InitialChat)
admin.site.register(RegisteredPerson)
admin.site.register(DailyUpdate)
admin.site.register(Web_Registration)
# Register your models here.
