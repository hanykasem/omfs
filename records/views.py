from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the OMFS Case Records Platform!</h1>")