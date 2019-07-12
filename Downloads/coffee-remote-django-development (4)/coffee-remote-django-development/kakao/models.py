from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Payment(models.Model):
    aid = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DateTimeField(default=timezone.now)
    created_at= models.IntegerField()
    # pickuptime = models.IntegerField()
    approved_at = models.CharField(max_length=50)
    tid = models.CharField(
        max_length=30,
        null=True
    )
    is_paid = models.BooleanField(default=False)
