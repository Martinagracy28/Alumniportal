from django.shortcuts import render,redirect
from . import views
from .models import Person
from .forms import *

# Create your views here.
def home(request):
    p = Person()
    if request.method == "POST":
        p.name = request.POST['name']
        p.phoneno = request.POST['phoneno']
        p.address = request.POST['address']
        
        p.save()

        person = Person.objects.all()
        return render(request,'home.html',{'person':person})

    else:
        person= Person.objects.all()
        return render(request, 'home.html',{'person':person})

def view(request,pk):
    person= Person.objects.get(id=pk)
    return render(request, 'view.html',{'person':person})

def update(request,pk):

    person = Person.objects.get(id=pk)
    form = PersonForm(instance = person)
    if request.method == "POST":
        form = PersonForm(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        return render(request,'update.html',{'form':form})  

def delete(request,pk):
    person = Person.objects.get(id=pk)
    person.delete()
    person = Person.objects.all()
    return render(request,'home.html',{'person':person})
                    
