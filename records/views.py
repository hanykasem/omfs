from django.http import Http404
from django.shortcuts import render
from .models import Patient

def index(request):
    all_patients = Patient.objects.all()
    return render(request, 'records/index.html', {'all_patients': all_patients})

def detail(request, record_id):
    try:
        patient = Patient.objects.get(pk=record_id)
    except Patient.DoesNotExist:
        raise Http404("Record does not exist")
    return render(request, 'records/detail.html', {'patient': patient})
