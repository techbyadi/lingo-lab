from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('words/', views.word_index, name='word-index'),
  path('words/<int:word_id>/', views.word_detail, name='word-detail'),
  path('words/create/', views.WordCreate.as_view(), name='word-create'),
  path('words/<int:pk>/update/', views.WordUpdate.as_view(), name='word-update'),
  path('words/<int:pk>/delete/', views.WordDelete.as_view(), name='word-delete'),
]