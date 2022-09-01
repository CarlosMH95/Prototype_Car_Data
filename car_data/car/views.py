from django.shortcuts import render

# Create your views here.
from .models import CarData
from rest_framework import generics
from .serializers import CarDataSerializer


def index(request):
    return render(request, 'car/index.html')

class CarDataCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new CarData
    queryset = CarData.objects.all(),
    serializer_class = CarDataSerializer

class CarDataList(generics.ListAPIView):
    # API endpoint that allows CarData to be viewed.
    queryset = CarData.objects.all().order_by('-created')
    serializer_class = CarDataSerializer

class CarDataDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single CarData by pk.
    queryset = CarData.objects.all()
    serializer_class = CarDataSerializer

class CarDataUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a CarData record to be updated.
    queryset = CarData.objects.all()
    serializer_class = CarDataSerializer

class CarDataDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a CarData record to be deleted.
    queryset = CarData.objects.all()
    serializer_class = CarDataSerializer
