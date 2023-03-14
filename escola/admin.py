from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'data_nacimento')
    list_display_links = ('id', 'nome')
  #  search_fields = ('nome')
    list_per_page = (20)

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'nivel')
    list_display_links = ('codigo', 'descricao')
   # search_fields = ('codigo')
    list_per_page = (20)

admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'periodo')
    list_display_links = ('aluno', 'curso')
   # search_fields = ('codigo')
    list_per_page = (20)

admin.site.register(Matricula, Matriculas)