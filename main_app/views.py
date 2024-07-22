from django.shortcuts import render
from django.views import generic
from .models import Movies

# Create your views here.
class MovieList(generic.ListView):
    queryset = Movies.objects.all()
    template_name = "main_app/index.html"
    paginate_by = 6
