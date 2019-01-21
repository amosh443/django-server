from proj.app import models
from proj.app import serializers
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class CafeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cafes to be viewed or edited.
    """
    queryset = models.Cafe.objects.all()
    serializer_class = serializers.CafeSerializer


class DishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dishes to be viewed or edited.
    """
    queryset = models.Dish.objects.all()
    serializer_class = serializers.DishSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = models.Order.objects.all()
    serializer_class = serializers.CafeSerializer
