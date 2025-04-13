from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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

class AppReview(models.Model):
    app = models.ForeignKey(firstappVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.app.name} - {self.rating}'

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    app_varity = models.ManyToManyField(firstappVarity, related_name='stores')

    def __str__(self):
        return self.name

class AppCertificate(models.Model):
    app = models.OneToOneField(firstappVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.app.name}'