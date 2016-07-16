from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Patient

class IndexView(generic.ListView):
    template_name = 'records/index.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return Patient.objects.all()

class DetailView(generic.DetailView):
    model = Patient
    template_name = 'records/detail.html'

class PatientCreate(CreateView):
    model = Patient
    fields = ['name', 'pid', 'date_of_birth', 'medical_history', 'presentation_date', 'presentation']