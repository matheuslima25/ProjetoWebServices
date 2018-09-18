from django.contrib import admin

from publicacoes.models import Publicacao, Categoria
admin.site.register(Categoria)


@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'imagem', 'titulo', 'mensagem', 'dt_criacao', 'categoria')
    search_fields = ('mensagem', 'usuario__email', )
    list_filter = ('usuario', 'dt_criacao', )

    fieldsets = (
        (None, {
            'fields': ('imagem', 'titulo', 'mensagem', 'categoria')
        }),
        ("Dados", {
            'fields': (('dt_criacao', 'dt_atualizacao', ), )
        }),
    )
    readonly_fields = ('dt_criacao', 'dt_atualizacao', )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(usuario=request.user)
