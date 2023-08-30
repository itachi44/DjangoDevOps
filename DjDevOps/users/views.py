from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    users = Account.objects.all()
    return render(request, 'users/index.html', {'users': users})
