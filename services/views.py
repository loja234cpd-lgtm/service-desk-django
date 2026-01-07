from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]

from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdmin

permission_classes = [IsAuthenticated, IsAdmin]