from django.shortcuts import render

finches = [
  {'name': 'Lolo', 'subfamily': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'subfamily': 'calico', 'description': 'gentle and loving', 'age': 2},
]

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
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'finches/finches_index.html', {
    'finches': finches
  }) 
