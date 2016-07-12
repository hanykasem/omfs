from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the OMFS Case Records Platform!</h1>")

def detail(request, record_id):
    return HttpResponse("<h2>Record detail page for ID number: " + str(record_id) + "</h2>")
