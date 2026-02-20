from django.db import models

class Entradas(models.Model):
    data = models.DateField()
    origem = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origem} - {self.valor}"

class Gasto(models.Model):
    tipo_escolha = [
        ('dinheiro', 'Dinheiro'),
        ('pix', 'Pix'),
    ]

    nome = models.CharField(max_length=100)
    registro = models.DateTimeField()
    tipo = models.CharField(choices=tipo_escolha, default='dinheiro')
    categoria = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"O gasto é {self.nome}"