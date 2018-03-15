from django.shortcuts import render
from .models import Board
from django.utils.translation import activate
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _


def home(request):

    boards = Board.objects.all()
   # target_language='de'
    #activate(target_language)
	
#Return the page home.html 
    return render(request, 'home.html', {'boards': boards})

def testlang(request):
    return HttpResponse(_('Hello, Hello'))

