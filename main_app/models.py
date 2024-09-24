from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Word(models.Model):
    word = models.CharField(max_length=20)
    origin = models.CharField(max_length=50)
    usage_in_sentence = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word