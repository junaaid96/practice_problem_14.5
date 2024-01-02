from django.shortcuts import render
from .forms import SecondForm

# Create your views here.


def index(request):
    another_form = SecondForm()
    return render(request, 'index.html', {'another_form': another_form})
