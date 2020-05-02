from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import InitialChat,RegisteredPerson,DailyUpdate
from .serializers import InitialChatSerializer,RegisteredPersonSerializer,DailyUpdateSerializer
from django.shortcuts import render

class CheckAllChats(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        a=InitialChat.objects.all()
        data=InitialChatSerializer(a,many=True).data
        return Response(data)

    def post(self,request):
        serializer=InitialChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("created")
        return Response("failed")


class CheckInitialChats(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        a=InitialChat.objects.filter(person_id=pk)
        if len(a)==0:
            return Response(-4)
        else:
            return Response(a[0].stage)

    def put(self,request,pk):
        snippet = InitialChat.objects.filter(person_id=pk)[0]
        serializer = InitialChatSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("updated")
        return Response("failed")

class RegisterPeopleAll(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        a=RegisteredPerson.objects.all()
        data = RegisteredPersonSerializer(a,many=True).data
        return Response(data)

    def post(self,request):
        serializer = RegisteredPersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("created")
        return Response("failed")

class DailyUpdateAll(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        a=DailyUpdate.objects.all()
        data = DailyUpdateSerializer(a,many=True).data
        return Response(data)

    def post(self, request):
        serializer = DailyUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("created")
        return Response("failed")

def show_details(request):
    if request.method=='GET':
        return render(request,"index.html")

def show_listings(request):
    if request.method=='GET':
        return render(request,"listings.html")