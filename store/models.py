from django.db import models
from  django_pg.models import BaseOrder
from django.contrib.auth.models import User

class Order(BaseOrder):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivered_date = models.DateTimeField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)