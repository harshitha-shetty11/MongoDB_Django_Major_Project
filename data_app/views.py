# Create your views here.
from django.shortcuts import render, redirect 
from .forms import PersonForm 
from .models import Person 


def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_people')  # Redirect to the list page after saving
    else:
        form = PersonForm()
    return render(request, 'data_app/add_person.html', {'form': form})


def list_people(request):
    people = Person.objects.all()  # Retrieve all data from the Person collection
    return render(request, 'data_app/list_people.html', {'people': people})