from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Word
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def word_index(request):
  words = Word.objects.filter(user=request.user).order_by('-date_added') 
  return render(request, 'words/index.html', {'words': words})

@login_required
def word_detail(request, word_id):
  word = Word.objects.get(id=word_id)
  return render(request, 'words/detail.html', {'word': word})

class WordCreate(LoginRequiredMixin, CreateView):
  model = Word
  fields = ['word', 'meaning', 'synonyms', 'usage_in_sentence']  
  success_url = '/words/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WordUpdate(LoginRequiredMixin, UpdateView):
  model = Word
  fields = ['word', 'meaning', 'synonyms', 'usage_in_sentence']
  success_url = '/words/'

class WordDelete(LoginRequiredMixin, DeleteView):
  model = Word
  success_url = '/words/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('word-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)