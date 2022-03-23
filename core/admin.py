from django.contrib import admin
from .models import Cliente



class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cidade')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cidade', 'id', 'cep', 'pais', 'endereco')



admin.site.register(Cliente, ClienteAdmin)
