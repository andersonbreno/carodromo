# Generated by Django 4.2 on 2023-04-16 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=10, unique=True)),
                ('serie', models.CharField(max_length=50)),
                ('imagem', models.ImageField(upload_to='alunos/')),
            ],
        ),
    ]
