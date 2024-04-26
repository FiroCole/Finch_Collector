from django.shortcuts import render, redirect
from .models import Finch, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

# Define the about view
def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

# Define the home view
def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/finches_index.html', {
    'finches': finches
  }) 
  
def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.songs.all().values_list('id')
  songs_finch_doesnt_have = Song.objects.exclude(id__in=id_list)
  
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {
    'finch': finch, 'feeding_form': feeding_form, 'songs':songs_finch_doesnt_have
  }) 

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)
  
class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'subfamily', 'description', 'habitat']
  success_url = '/finches/{id}'
  
class FinchUpdate(UpdateView):
  model = Finch
  fields = ['subfamily', 'description', 'habitat']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'
  
class SongList(ListView):
  model = Song

class SongDetail(DetailView):
  model = Song

class SongCreate(CreateView):
  model = Song
  fields = '__all__'

class SongUpdate(UpdateView):
  model = Song
  fields = ['song']

class SongDelete(DeleteView):
  model = Song
  success_url = '/songs'
  
  
def assoc_song(request, finch_id, song_id):
  Finch.objects.get(id=finch_id).songs.add(song_id)
  return redirect('detail', finch_id=finch_id)