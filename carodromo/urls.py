from django.urls import path
from .views import aluno_list, aluno_add, testar, aluno


urlpatterns = [
    path('', aluno_list, name='aluno_list'),
    path('adicionar_aluno/', aluno_add, name='aluno_add'),
    path('aluno/<int:pk>', aluno, name='aluno'),
    path('teste/', testar, name='teste'),
]
