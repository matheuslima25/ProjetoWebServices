from django.contrib import admin

from .models import Atracao
admin.site.register(Atracao)


class Atracoes(admin.ModelAdmin):
    list_display = ('name', 'profissao')

