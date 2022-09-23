
from django.shortcuts import render
from .forms import CandidatForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method=="POST":
        form = CandidatForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'ajout du candidat reussi')
            return HttpResponseRedirect('/')
        else:
            return render(request, "index.html", {'form': form})
    else:
        form=CandidatForm()
        return render(request, "index.html", {'form': form})