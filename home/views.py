from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return index page """
    return render(request, 'home/index.html')

def our_work(request):
    """ A view to return the work page to showcase designs """
    return render(request, 'home/work.html')