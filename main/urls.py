from django.urls import path
from . import views

urlpatterns = [
    path("create-room/", views.RoomCreate.as_view()),
    path("update-room/<int:pk>/", views.UpdateRoom.as_view()),
    path("delete-room/<int:pk>/", views.DeleteRoom.as_view()),
]