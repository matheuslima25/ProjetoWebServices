from django.urls import path

from django.contrib.auth.views import LoginView

from meuPrimeiroProjeto import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('entrar/', LoginView.as_view(template_name='meuPrimeiroProjeto/login.html'), name='entrar'),
]
