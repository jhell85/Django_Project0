from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
  movies = Movie.objects.all()

  context = {
    'movies': movies
  }
  print(context)
  return render(request, 'myapp/index.html', context)
# Create your views here.
