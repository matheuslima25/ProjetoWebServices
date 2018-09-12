from django.contrib import admin, messages

from publicacoes.models import Publicacao


@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mensagem', 'dt_criacao', )
    search_fields = ('mensagem', 'usuario__email', )
    list_filter = ('usuario', 'dt_criacao', )

    fieldsets = (
        (None, {
            'fields': ('mensagem', )
        }),
        ("Dados", {
            'fields': (('dt_criacao', 'dt_atualizacao', ), )
        }),
    )
    readonly_fields = ('dt_criacao', 'dt_atualizacao', )
    actions = ('atualizar_action', )

    def atualizar_action(self, request, queryset):
        for p in queryset:
            p.mensagem += "..."
            p.save()
        messages.info(request, "Publicações atualizadas com sucesso!")
    atualizar_action.short_description = "Atualizar com ..."

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(usuario=request.user)
