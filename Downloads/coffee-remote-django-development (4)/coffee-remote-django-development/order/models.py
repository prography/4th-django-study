from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()
    # pickuptime = models.IntegerField()
    order = models.CharField(max_length=50)
    tid = models.CharField(
        max_length=30,
        null=True
    )
    is_paid = models.BooleanField(default=False)



# unique_id : 아이디(string)
# price : 총 가격(int)
# pickuptime : 5 또는 10 (int)
# order : 메뉴id,수량;(string) ex> "3,5;4,1;"

# pickup -

# admin
