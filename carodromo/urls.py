from django.urls import path
from .views import index, aluno, aluno_add, aluno_6ano, aluno_7ano, aluno_8ano, aluno_9ano


urlpatterns = [
    path('', index, name='index'),
    path('adicionar_aluno/', aluno_add, name='aluno_add'),
    path('aluno_6ano/', aluno_6ano, name='aluno_6aluno'), 
    path('aluno_7ano/', aluno_7ano, name='aluno_7ano'), 
    path('aluno_8ano/', aluno_8ano, name='aluno_8ano'),
    path('aluno_9ano/', aluno_9ano, name='aluno_9ano'),
    path('aluno/<int:id>/', aluno, name='aluno'),
]
