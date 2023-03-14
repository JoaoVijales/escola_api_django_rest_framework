from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet


router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
