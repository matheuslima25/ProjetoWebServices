from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from meuPrimeiroProjeto import views

urlpatterns = [
    path('', views.HomeView.as_view()),
]
