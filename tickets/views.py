from rest_framework.viewsets import ModelViewSet
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.select_related(
        'client', 'service', 'technician'
    )
    serializer_class = TicketSerializer
