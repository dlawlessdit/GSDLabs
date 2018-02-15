from django.shortcuts import render
from .models import Board

def home(request):
    boards = Board.objects.all()
#Return the page home.html 
    return render(request, 'home.html', {'boards': boards})

