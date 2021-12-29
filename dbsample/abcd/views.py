from django.shortcuts import render
from django.http import HttpResponse
def ab(request):
    message="pass"
    return HttpResponse(message)

# Create your views here.
