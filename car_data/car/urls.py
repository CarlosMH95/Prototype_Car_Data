from django.urls import path
from .views import CarDataCreate, CarDataList, CarDataDetail, CarDataUpdate, CarDataDelete, index, CarDataListLast10, chartData, line_chart, line_chart_json


urlpatterns = [
    path('create/', CarDataCreate.as_view(), name='create-CarData'),
    path('', CarDataList.as_view()),
    path('last/', CarDataListLast10.as_view()),
    path('<int:pk>/', CarDataDetail.as_view(), name='retrieve-CarData'),
    path('update/<int:pk>/', CarDataUpdate.as_view(), name='update-CarData'),
    path('dashboard/',index, name='dashboard-CarData'),
    path('charts/',chartData, name='chart-CarData'),
    path('chart/', line_chart, name='line_chart'),
    path('chartJSON/', line_chart_json, name='line_chart_json'),
    # path('delete/<int:pk>/', CarDataDelete.as_view(), name='delete-CarData')
]