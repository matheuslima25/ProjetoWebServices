from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    nome = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='filho', on_delete=models.CASCADE)

    def __str__(self):
        full_path = [self.nome]

        k = self.parent

        while k is not None:
            full_path.append(k.nome)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Publicacao(models.Model):
    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"
        ordering = ('-dt_criacao', )

    usuario = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', null=True, blank=True, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30, verbose_name="Título", help_text="Digite um título", blank=True, null=True)
    imagem = models.ImageField(verbose_name="Imagem", upload_to="publicacoes", blank=True, null=True)
    mensagem = models.TextField(verbose_name="Mensagem", help_text="Digite uma mensagem", blank=True)

    dt_criacao = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    dt_atualizacao = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)

    def teste(self):
        return "ID da mensagem é %s" % self.id

    def __str__(self):
        return "%s: %s" % (self.usuario, self.mensagem)

    def get_cat_list(self):
        k = self.categoria
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]