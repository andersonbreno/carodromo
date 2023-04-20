from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'serie', 'matricula', 'imagem']

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']
        if Aluno.objects.filter(matricula=matricula).exists():
            raise forms.ValidationError("Já existe um aluno com essa matrícula.")
        return matricula    
