from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm


def index(request):
    return render(request, 'index.html')

def aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, 'aluno.html', {'aluno': aluno})

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

def aluno_7ano(request):
    aluno_7ano = Aluno.objects.filter(serie='7')

    context = {
        'aluno_7ano': aluno_7ano 
    }
    return render(request, '7ano.html', context)  

def aluno_8ano(request):
    aluno_8ano = Aluno.objects.filter(serie='8')

    context = {
        'aluno_8ano': aluno_8ano 
    }
    return render(request, '8ano.html', context)    

def aluno_9ano(request):
    aluno_9ano = Aluno.objects.filter(serie='9')

    context = {
        'aluno_9ano': aluno_9ano 
    }
    return render(request, '9ano.html', context)      



