from django.shortcuts import render
from django.views import generic
from .models import Movies

# Create your views here.
class MovieList(generic.ListView):
    model = Movies
