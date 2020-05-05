from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import InitialChat,RegisteredPerson,DailyUpdate,Web_Registration
from .serializers import InitialChatSerializer,RegisteredPersonSerializer,DailyUpdateSerializer
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

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
        person_id=request.data["person_id"]
        person = RegisteredPerson.objects.filter(person_id=person_id)[0]
        b=DailyUpdate.objects.create(person=person,shop_open=request.data["shop_open"],mask_avail=request.data["mask_avail"],sanitizer_avail=request.data["sanitizer_avail"])
        return Response("created")



@csrf_exempt
def show_details(request):
    if request.method=='GET':
        return render(request,"index.html")
    else:
        a=Web_Registration.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],contact_name=request.POST['contact_name'],shop_owner=request.POST["shop_owner"],mask_avail=request.POST['mask_avail'],mask_price=request.POST['mask_price'],sanitizer_avail=request.POST["sanitizer_avail"],sanitizer_price=request.POST['sanitizer_price'],shop_name=request.POST['shop_name'],address=request.POST['address'],pincode=request.POST['pincode'])
        return HttpResponse("you")

def show_data(request,pk):
    if request.method=='GET':
        persons = RegisteredPerson.objects.filter(pincode=str(pk))
        b = []
        for person in persons:
            query = person.daily.all()
            if len(query) != 0:
                b.append(query[len(query)-1])
        if len(b)==0:
            key=0
        else:
            key=1

        return render(request,"listings.html",{"shops":b,"pincode":str(pk),'key':key})

@csrf_exempt
def register_shop(request):
    if request.method=='GET':
        return render(request,"index1.html")
    else:
        print(request.POST)
        a=Web_Registration.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],contact_name=request.POST['contact_name'],shop_owner=request.POST["shop_owner"],mask_avail=request.POST['mask_avail'],mask_price=request.POST['mask_price'],sanitizer_avail=request.POST["sanitizer_avail"],sanitizer_price=request.POST['sanitizer_price'],shop_name=request.POST['shop_name'],address=request.POST['address'],pincode=request.POST['pincode'])
        return HttpResponse("you")