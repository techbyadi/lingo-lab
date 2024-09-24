from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('words/', views.word_index, name='word-index'),
  path('words/<int:word_id>/', views.word_detail, name='word-detail'),
]