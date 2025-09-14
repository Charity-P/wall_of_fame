from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    full_name = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    registration_number = models.CharField(max_length=20, unique=True)
    country = models.CharField(max_length=50)
    learning_track = models.CharField(max_length=200)
    linkedin = models.URLField(blank=False, null=False)
    github = models.URLField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     # make sure password is always hashed
    #     if not self.password.startswith("pbkdf2_"):
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.registration_number})"


# class Visitor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     partner = models.BooleanField()
#     organisation_name = models.CharField(max_length=250)
