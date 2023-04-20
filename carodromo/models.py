from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10, unique=True)
    serie = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='alunos/')

    def __str__(self):
        return self.nome

