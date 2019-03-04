from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Sean. You're at the polls index.")