from rest_framework import serializers
from escola.models import Curso, Aluno


class AlunoSerializer(serializers.ModelSerializer):
    
    class Meta:     
        model: Aluno
        fields: '__all__'



class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:     
        model: Curso
        fields: '__all__'
        