from django.contrib import admin
from escola.models import Alunos, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'data_nacimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome')
    list_per_page = (20)
