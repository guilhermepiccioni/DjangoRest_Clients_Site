from django.db import models


class Cliente(models.Model):
    # objects = None
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=50)
    cep = models.IntegerField()
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
