from django.db import models

# Create your models here.

class Pessoa(models.Model):
    GENEROS = (
        ('M', 'Masculinio'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )

    nome = models.CharField(
        max_length=30,
        verbose_name='Nome'
    )
    sobrenome = models.CharField(
        max_length=255,
        verbose_name='Sobrenome'
    )
    genero = models.CharField(
        max_length=255,
        verbose_name = 'Gênero',
        choices = GENEROS
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='E-mail'
    )

    # campo de data e hora - auto_now_add==
    # busca de onde ta conectado a sua aplicacao e coloca a data e hora
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome+' '+self.sobrenome