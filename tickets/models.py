from django.db import models

class Ticket(models.Model):

    STATUS_CHOICES = (
        ('OPEN', 'Aberta'),
        ('IN_PROGRESS', 'Em andamento'),
        ('DONE', 'Concluída'),
        ('CANCELED', 'Cancelada'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    service = models.ForeignKey(
        'services.Service',
        on_delete=models.PROTECT,
        related_name='tickets'
    )

    technician = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role': 'TECH'},
        related_name='assigned_tickets'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'#{self.id} - {self.title}'
