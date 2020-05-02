from django.contrib import admin
from django.urls import path
from .views import CheckAllChats,CheckInitialChats,RegisterPeopleAll,DailyUpdateAll
from . import views
urlpatterns = [
    path('api/all/',CheckAllChats.as_view()),
    path('api/check/<int:pk>/',CheckInitialChats.as_view()),
    path('api/reg/all/',RegisterPeopleAll.as_view()),
    path('api/update/all/',DailyUpdateAll.as_view()),
    path('',views.show_details,name='show_details'),
    path('listings/',views.show_listings,name='show_listings'),

]

