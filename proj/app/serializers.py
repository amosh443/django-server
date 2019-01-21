from proj.app import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('name', 'surname', 'password', 'phone', 'card')


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cafe
        fields = ('name', 'description', 'password', 'phone', 'photo', 'coord_x', 'coord_y', 'dishes')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dish
        fields = ('name', 'description', 'photo')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('user_id', 'cafe_id', 'time', 'giving', 'comment', 'count', 'status', 'dishes')
