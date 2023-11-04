from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class user_model(User):
    phone = models.PositiveBigIntegerField(unique=True)
    gender = models.CharField(max_length=10, choices=[
                              ['male', 'male'], ['female', 'female']])
    dob = models.DateField()
