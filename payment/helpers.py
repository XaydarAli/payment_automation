from django.db import models

class PaymentStatus(models.TextChoices):
    Pending = 'Pending', 'Pending'
    PROCESSING = 'PROCESSING','Processing'
    Canceled = 'CANCELED', 'Canceled'
    REJECTED = 'REJECTED','Rejecting'
    Succeeded = 'SUCCEEDED','Succeeded'