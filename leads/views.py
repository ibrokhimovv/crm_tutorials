from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . import models
from .forms import *

def leads_list(request):
    leads = models.Lead.objects.all()

    context = {
        "leads": leads
    }
    return render(request, 'leads_list.html', context)

def leads_detail(request, pk):
    lead = get_object_or_404(models.Lead, id=pk)
    context = {
        "lead": lead
    }
    return render(request, 'templates/details.html', context)

def create_load(request):
    context = {
        'forms': LeadForm()
    }

    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sourname = form.cleaned_data['sourname']
            age = form.cleaned_data['age']
            agent = models.Agent.objects.first()
            models.Lead.objects.create(
                name=name,
                sourname=sourname,
                age=age,
                agent=agent
            )

    return render(request, 'templates/create.html', context)