from django.db import models

class Cartao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    parcela = models.IntegerField()
    categoria = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"A conta do cartão é {self.nome}"