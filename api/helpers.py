
from django.db import models




class StatusChoices(models.TextChoices):
    DRAFT = 'df', 'Draft'
    Published = 'pb', 'Published'