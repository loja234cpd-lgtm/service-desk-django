from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Client
from .serializers import ClientSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]

from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdmin

permission_classes = [IsAuthenticated, IsAdmin]

