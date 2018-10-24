from django import forms

from publicacoes.models import Inscricao


class InscForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ('nome', 'idade', 'email', 'categoria',)

    def save(self):
        inscricao = Inscricao.objects.create_inscricao(self.cleaned_data['nome'],
                                                       idade=self.cleaned_data['idaded'],
                                                       email=self.cleaned_data['email'],
                                                       categoria=self.cleaned_data['categoria'])
        return inscricao
