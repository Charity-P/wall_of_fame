from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='student_photos/')
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    student_id = models.CharField(max_length=20, unique=True)
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
        return f"{self.full_name} ({self.student_id})"

    # def __str__(self):
    #     return self.user.get_full_name()
