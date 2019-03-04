from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Tellim Drachir. You're at the polls index.")
