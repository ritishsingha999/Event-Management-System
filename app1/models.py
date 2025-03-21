from django.db import models

# Create your models here.
# ----------------------------------------
# Event
# Participant
# Category

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(unique=True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    EVENT_STATUS_CHOICES = [
        ('upcoming', 'upcoming'),
        ('ongoing', 'ongoing'),
        ('completed', 'completed'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image= models.ImageField(default='static/image/Monochrome Minimalist Live Music Event Facebook Post.png', blank=True, null=True)
    # notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=EVENT_STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

