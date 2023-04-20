from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculas, ListaAlunoMatriculado
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculas.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunoMatriculado.as_view()),
]
