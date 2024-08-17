from django.db import models
from django.utils import timezone

from payment.helpers import PaymentStatus


class PaymentCourse(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    course_id = models.PositiveIntegerField()
    student_id = models.PositiveIntegerField()
    status=models.CharField(max_length=10, choices=PaymentStatus.choices,default=PaymentStatus.Pending)
    publish=models.DateTimeField(default=timezone.now)
