from django.db import models


class Atracao (models.Model):
    class Meta:
        verbose_name = "Atração"
        verbose_name_plural = "Atrações"

    foto = models.ImageField(verbose_name="Foto")
    name = models.CharField(max_length=30, verbose_name="Nome")
    profissao = models.CharField(max_length=30, verbose_name= "Profissão")
    bio = models.TextField(verbose_name="Biografia", default="Uma breve descrição sobre a atração.")
    site = models.URLField(verbose_name="Site", default="ex: instagram.com/")


    def __str__(self):
        return self.name #edita a forma que é visto na lista dos usuarios

