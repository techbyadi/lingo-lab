from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Word:  
  def __init__(self, word, origin, usage_in_sentence):
    self.word = word
    self.origin = origin
    self.usage_in_sentence = usage_in_sentence

words = [
  Word('First', 'Greek', 'It\'s first word'),
  Word('Second', 'Greek', 'Looks like a second word.'),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Word!</h1>')

def about(request):
  return render(request, 'about.html')

def word_index(request):
  return render(request, 'words/index.html', { 'words': words })