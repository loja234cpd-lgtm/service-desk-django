from django.db import models

class Client(models.Model):
    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='client_profile'
    )
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name

