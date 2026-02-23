from django.db import models

class Fixos(models.Model):
    tipo_escolha = [
        ('assinatura', 'Assinatura'),
        ('conta', 'Conta')
    ]

    nome = models.CharField(max_length=100)
    data = models.DateField()
    tipo = models.CharField(choices=tipo_escolha, default='conta')
    categoria = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"O fixo é {self.nome}"