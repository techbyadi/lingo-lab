from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=20)
    origin = models.CharField(max_length=50)
    usage_in_sentence = models.TextField()

    def __str__(self):
        return self.word