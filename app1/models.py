# app1/models.py

from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    text = models.TextField()
    time_limit = models.IntegerField()  # in seconds

    def __str__(self):
        return self.text[:50]  # Return first 50 characters of the question text

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField()
    is_draft = models.BooleanField(default=True)
    submission_time = models.DateTimeField(auto_now=True)
    session = models.ForeignKey(UserSession, on_delete=models.CASCADE)

from django.contrib.auth.hashers import make_password


class UserRegistration(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserRegistration, self).save(*args, **kwargs)
