from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('status', 'created_at', 'updated_at')

    def create(self, validated_data):
        request = self.context['request']
        user = request.user

        if user.role == 'CLIENT':
            validated_data['client'] = user.client_profile

        return super().create(validated_data)
