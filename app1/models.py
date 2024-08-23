from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    text = models.TextField()
    time_limit = models.IntegerField()  # in seconds

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
