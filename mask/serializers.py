from rest_framework import serializers
from .models import InitialChat,RegisteredPerson,DailyUpdate

class InitialChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialChat
        fields="__all__"

class RegisteredPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= RegisteredPerson
        fields= "__all__"

class DailyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= DailyUpdate
        fields="__all__"