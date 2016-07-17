from django import forms
from django.contrib.auth.models import User

from .models import Patient, Visit


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['name', 'pid', 'date_of_birth', 'medical_history', 'presentation_date', 'presentation']


class VisitForm(forms.ModelForm):

    class Meta:
        model = Visit
        fields = ['visit_date', 'visit_note']