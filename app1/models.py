from django.db import models

# Create your models here.
# ----------------------------------------
# Event
# Participant
# Category

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

