from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import ListaAlunosMatriculadosSerializer ,AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class AlunosViewSet(viewsets.ModelViewSet): 
    
    """Exibindo todos alunos e alunas"""
    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
class CursosViewSet(viewsets.ModelViewSet): 
    
    """Exibindo todos os cursos"""
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet): 
    
    """Exibindo todos as matriculas"""
    
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class listaMatriculasAluno(generics.ListAPIView):
    
    """Listando as matriculas de um aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_class = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando as alunos e alunas matriculados em um curso"""
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
