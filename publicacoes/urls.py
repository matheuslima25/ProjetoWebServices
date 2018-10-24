from django.urls import path

from django.contrib.auth.views import LoginView

from publicacoes import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('index', views.HomeView.as_view(template_name='meuPrimeiroProjeto/index.html'), name='index'),
    path('entrar/', LoginView.as_view(template_name='meuPrimeiroProjeto/login.html'), name='entrar'),
    path('programacao', views.ProgramacaoView.as_view(template_name='meuPrimeiroProjeto/programacao.html'),
         name='programacao'),
    path('inscricoes', views.InscricaoView.as_view(template_name='meuPrimeiroProjeto/inscricoes.html'), name='inscricoes'),
    path('atracoes', views.AtracaoView.as_view(template_name='meuPrimeiroProjeto/atracoes.html'), name='atracoes'),
    path('patrocinadores', views.PatrocinadorView.as_view(template_name='meuPrimeiroProjeto/patrocinadores.html'), name='patrocinadores'),

]
