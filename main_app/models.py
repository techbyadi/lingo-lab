from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Word(models.Model):
    word = models.CharField(max_length=20)
    meaning = models.CharField(max_length=100)
    synonyms = models.CharField(max_length=100)
    usage_in_sentence = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.word
    
    def get_absolute_url(self):
        return reverse('word-detail', kwargs={'word_id': self.id})