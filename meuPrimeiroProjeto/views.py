from django.http import HttpResponse
from atracoes import models

def atracoes (request):
    return HttpResponse(models.Atracao)

