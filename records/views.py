from django.http import HttpResponse
from django.template import loader
from .models import Patient

def index(request):
    all_patients = Patient.objects.all()
    template = loader.get_template('records/index.html')
    context = {
        'all_patients': all_patients,
    }
    return HttpResponse(template.render(context, request))

def detail(request, record_id):
    return HttpResponse("<h2>Record detail page for ID number: " + str(record_id) + "</h2>")
