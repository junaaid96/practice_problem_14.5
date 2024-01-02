from django.shortcuts import render
from first_app.forms import firstForm

# Create your views here.


def home(request):
    first_form = firstForm()
    if request.method == 'POST':
        first_form = firstForm(request.POST)
        if first_form.is_valid():
            print("Name: " + first_form.cleaned_data['name'])
            print("Email: " + first_form.cleaned_data['email'])
            print("Comment: " + first_form.cleaned_data['comment'])
    return render(request, 'home.html', {'form': first_form})
