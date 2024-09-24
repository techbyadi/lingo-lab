from django.shortcuts import render
from django.http import HttpResponse
from .models import Word

class Word_old:  
  def __init__(self, word, origin, usage_in_sentence):
    self.word = word
    self.origin = origin
    self.usage_in_sentence = usage_in_sentence

words_old = [
  Word('First', 'Greek', 'It\'s first word'),
  Word('Second', 'Greek', 'Looks like a second word.'),
]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def word_index(request):
  words = Word.objects.all()
  return render(request, 'words/index.html', {'words': words})