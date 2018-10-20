from django.views.generic import ListView

from publicacoes.models import Publicacao


class HomeView(ListView):
    template_name = 'meuPrimeiroProjeto/index.html'
    model = Publicacao

