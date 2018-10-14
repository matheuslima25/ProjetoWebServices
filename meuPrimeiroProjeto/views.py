from django.contrib.auth import login
from django.views.generic import ListView, FormView

from publicacoes.models import Publicacao


class HomeView(ListView):
    template_name = 'meuPrimeiroProjeto/index.html'
    model = Publicacao

