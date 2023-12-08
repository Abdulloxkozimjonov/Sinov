from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,DestroyAPIView
from . import models
from . import serializers

class RoomCreate(ListCreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class UpdateRoom(UpdateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class DeleteRoom(DestroyAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer