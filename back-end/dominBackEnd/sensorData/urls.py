from rest_framework import routers, serializers, viewsets
from .views import SensorDataViewSet

routes = [(r"sensorData", SensorDataViewSet)]