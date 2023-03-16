from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasSerializer


class AlunosViewSet(viewsets.ModelViewSet): 
    
    """Exibindo todos alunos e alunas"""
    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet): 
    
    """Exibindo todos os cursos"""
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet): 
    
    """Exibindo todos as matriculas"""
    
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer



class listaMatriculasAluno(generics.ListAPIView):
    
    """Listando as matriculas de um aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasSerializer
