from django.contrib import admin

from core.models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')
    list_filter = ('nome','preco',)
    search_fields = ('nome',)


#outra forma de registrar
#admin.site.register(Produto, ProdutoAdmin)