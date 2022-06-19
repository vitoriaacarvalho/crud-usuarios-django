from django.db import models

class Usuario(models.Model):
    nome=models.CharField(max_length=30)
    usuario=models.CharField(max_length=30)
    matricula=models.IntegerField()
    senha=models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.nome

# Create your models here.
