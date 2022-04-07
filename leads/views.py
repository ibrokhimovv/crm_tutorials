from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . import models

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