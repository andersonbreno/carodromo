
from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm


def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno_list.html', {'alunos': alunos})


def aluno_add(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm()
    return render(request, 'aluno_add.html', {'form': form})


def aluno(request, pk):
    aluno_listado = Aluno.objects.get(id=pk)

    context = {
        'aluno': aluno_listado 
    }
    return render(request, 'aluno.html', context)


def testar(request):
    context = {
        'teste': 'testando'
    }
    return render(request, 'teste.html', context)
