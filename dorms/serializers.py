from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Dorm, Room, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dorm
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

