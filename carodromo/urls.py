from django.urls import path
from .views import index, aluno_add, aluno_6ano


urlpatterns = [
    path('', index, name='index'),
    path('adicionar_aluno/', aluno_add, name='aluno_add'),
    path('aluno_6ano/', aluno_6ano, name='aluno_6aluno'),  
]
