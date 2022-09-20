from multiprocessing import context
from django.shortcuts import render
from .forms import CandidatForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def index(request):
    form = CandidatForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'ajout du candidat reussi')
        return HttpResponseRedirect('/')
    context = {
        'form': form,
    }
    return render(request, "index.html", context)
