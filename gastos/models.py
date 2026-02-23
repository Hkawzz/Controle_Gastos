from django.db import models

class Gastos(models.Model):
    tipo_escolha = [
        ('Dinheiro', 'Dinheiro'),
        ('Pix', 'Pix'),
        ('Débito', 'Débito'),
        ('Crédito', 'Crédito'),
        ('VR', 'VR'),
        ('VA', 'VA'),
    ]

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
    registro = models.DateTimeField()
    tipo = models.CharField(choices=tipo_escolha, default='Dinheiro', max_length=20)
    categoria = models.CharField(choices=categoria_escolha, default='Lazer', max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"O gasto é {self.nome}"