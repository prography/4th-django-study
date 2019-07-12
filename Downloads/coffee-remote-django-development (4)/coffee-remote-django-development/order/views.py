from order.models import Order
from rest_framework import viewsets
from order.serializers import OrderSerializer
# from django.shortcuts import render, redirect
# import requests
# import json

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
