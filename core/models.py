from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Carro(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='carros')
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    preco = models.FloatField()

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.cor} {self.ano}'
