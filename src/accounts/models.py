from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=False, unique=True)
    phone = models.CharField(max_length=13, null=False, unique=True)
    birdthday = models.DateField(null=False)
    age = models.FloatField(null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    language = models.CharField(max_length=2)
    status = models.CharField(max_length=20)

    # status = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=20)
    created_at = models.TimeField()
    updated_at = models.TimeField()

    def __str__(self):
        return f'Id {self.id}: {self.username}'
