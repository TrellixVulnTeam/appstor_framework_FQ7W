from django.db import models
from django.utils import timezone
class App(models.Model):
    STATUS_CHOICES = (
        ('p', 'pay'),
        ('n', 'without pay')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to = "images")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    priority = models.IntegerField()
    rateCounter = models.IntegerField()
    Rate = models.FloatField()
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    def __str__(self):
        return self.title