from django.shortcuts import render

# Create your views here.
from .models import CarData
from rest_framework import generics
from .serializers import CarDataSerializer
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        queryset = CarData.objects.all().order_by('-created')[:10]
        response = []
        for x in queryset:
            response.append(x.created.strftime('%Y-%m-%d %H:%M:%S'))
        response.reverse()
        return response

    def get_providers(self):
        """Return names of datasets."""
        return ["Temperatura", "Humedad",]

    def get_data(self):
        """Return 3 datasets to plot."""
        queryset = CarData.objects.all().order_by('-created')[:10]
        response1 = []
        response2 =[]
        for x in queryset:
            response1.append(x.temp)
            response2.append(x.humidity)
        response1.reverse()
        response2.reverse()
        return [response1,
                response2,]


line_chart = TemplateView.as_view(template_name='car/line_chart.html')
line_chart_json = LineChartJSONView.as_view()


def index(request):
    return render(request, 'car/index.html')

def chartData(request):
    
    return render(request, 'car/lineChart.html')

class CarDataCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new CarData
    queryset = CarData.objects.all(),
    serializer_class = CarDataSerializer

class CarDataList(generics.ListAPIView):
    # API endpoint that allows CarData to be viewed.
    queryset = CarData.objects.all().order_by('-created')
    serializer_class = CarDataSerializer

class CarDataListLast10(generics.ListAPIView):
    # API endpoint that allows CarData to be viewed.
    queryset = CarData.objects.all().order_by('-created')[:10]
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
