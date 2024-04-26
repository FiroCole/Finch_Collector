from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
  return render(request, 'finches/detail.html', {
    'finch': finch
  }) 

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches/{id}'
  
class FinchUpdate(UpdateView):
  model = Finch
  fields = ['subfamily', 'description', 'habitat']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'