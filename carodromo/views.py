
from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm


# def aluno_list(request):
#     alunos = Aluno.objects.all()
#     return render(request, 'aluno_list.html', {'alunos': alunos})

def index(request):
    return render(request, 'index.html')


def aluno_add(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlunoForm()
    return render(request, 'aluno_add.html', {'form': form})


def aluno_6ano(request):
    aluno_6ano = Aluno.objects.filter(serie='6')

    context = {
        'aluno_6ano': aluno_6ano 
    }
    return render(request, '6ano.html', context)



