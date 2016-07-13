from django.shortcuts import render, get_object_or_404
from .models import Patient

def index(request):
    all_patients = Patient.objects.all()
    return render(request, 'records/index.html', {'all_patients': all_patients})

def detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'records/detail.html', {'patient': patient})
