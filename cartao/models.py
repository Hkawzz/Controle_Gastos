from django.db import models

class Cartao(models.Model):
    categoria_escolha = [
        ('Moradia', 'Moradia'),
        ('Contas', 'Contas'),
        ('Mercados', 'Mercados'),
        ('Transporte', 'Transporte'),
        ('Saúde', 'Saúde'),
        ('Lazer', 'Lazer'),
        ('Restaurante', 'Restaurante'),
        ('Compras', 'Compras'),
        ('Assinatura', 'Assinatura'),
        ('Educação', 'Educação'),
        ('Imprevisto', 'Imprevisto'),
    ]

    nome = models.CharField(max_length=100)
    data = models.DateField()
    parcela = models.IntegerField()
    categoria = models.CharField(choices=categoria_escolha, default='Compras')
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"A conta do cartão é {self.nome}"