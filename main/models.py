from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=55)
    student_number = models.IntegerField(default=15)

    def __str__(self):
        return self.name
