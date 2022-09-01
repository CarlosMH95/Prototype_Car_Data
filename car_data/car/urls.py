from django.urls import path
from .views import CarDataCreate, CarDataList, CarDataDetail, CarDataUpdate, CarDataDelete, index


urlpatterns = [
    path('create/', CarDataCreate.as_view(), name='create-CarData'),
    path('', CarDataList.as_view()),
    path('<int:pk>/', CarDataDetail.as_view(), name='retrieve-CarData'),
    path('update/<int:pk>/', CarDataUpdate.as_view(), name='update-CarData'),
    path('dashboard/',index, name='dashboard-CarData'),
    # path('delete/<int:pk>/', CarDataDelete.as_view(), name='delete-CarData')
]