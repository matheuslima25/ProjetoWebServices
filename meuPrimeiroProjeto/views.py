from django.http import HttpResponse
from atracoes import models
from django.shortcuts import render

def home (request):
    return render(request, "index.html")

