from django.views.generic import ListView, FormView

from publicacoes.models import Publicacao, Programacao, Atracao, Patrocinador
from publicacoes.forms import InscForm


class HomeView(ListView):
    template_name = 'meuPrimeiroProjeto/index.html'
    model = Publicacao


class ProgramacaoView(ListView):
    template_name = 'meuPrimeiroProjeto/programacao.html'
    model = Programacao


class InscricaoView(FormView):
    template_name = 'meuPrimeiroProjeto/inscricoes.html'
    form_class = InscForm
    success_url = 'index'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AtracaoView(ListView):
    template_name = 'meuPrimeiroProjeto/atracoes.html'
    model = Atracao


class PatrocinadorView(ListView):
    template_name = 'meuPrimeiroProjeto/patrocinadores.html'
    model = Patrocinador
