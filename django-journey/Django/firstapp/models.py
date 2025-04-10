from django.db import models
from django.utils import timezone
# Create your models here.
class firstappVarity(models.Model):
    APP_CHOICE = [
        ('C', 'commercial'),
        ('P', 'personal'),
        ('E', 'enterprise'),
        ('B', 'business'),
        ('S', 'startup'),
        ('O', 'other'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_CHOICE, default='C')
    description = models.TextField(default='')

    def __str__(self) -> str:
        return self.name
    