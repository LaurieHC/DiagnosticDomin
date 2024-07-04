
from django.shortcuts import render
from .models import SensorData
from .serializers import SensorDataSerializer
from rest_framework import routers, serializers, viewsets
from .data_scripts import Scripts, get_event



class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    # search_fields = ['events']
    filterset_fields = {
      'timestamp':['gte', 'lte', 'exact', 'gt', 'lt'],
      'events':['exact']
    }

    def create(self, request, *args, **kwargs):


        request.data._mutable=True
        request.data["events"] = get_event(request.data)

        return super().create(request, *args, **kwargs)