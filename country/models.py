# country\models.py

from django.db import models

class Citizen(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    home_town = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name
