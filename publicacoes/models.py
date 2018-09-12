from django.contrib.auth.models import User
from django.db import models

class Publicacao(models.Model):
    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"
        ordering = ('-dt_criacao', )

    usuario = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=155, verbose_name="Mensagem", help_text="Digite uma mensagem")

    dt_criacao = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    dt_atualizacao = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)

    def teste(self):
        return "ID da mensagem é %s" % self.id

    def __str__(self):
        return "%s: %s" % (self.usuario, self.mensagem)
