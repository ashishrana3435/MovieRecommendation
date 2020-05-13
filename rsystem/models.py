from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100, db_index=True )
    rating = models.DecimalField(decimal_places=2, max_digits=4 )

# class UserData(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('T', 'Transgender'),
#         ('O', 'Other'),
#         ('N', 'Prefer Not to answer')
#     )
#     id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     age = models.IntegerField()

# class UserMovies(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.DecimalField(decimal_places=1, max_digits=4)

