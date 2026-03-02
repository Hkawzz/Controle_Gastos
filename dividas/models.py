from django.db import models
    
class Dividas(models.Model):
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
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(choices=categoria_escolha, default='Lazer')

    @property
    def total(self):
        return self.total_parcela * self.valor_parcela

    def __str__(self):
        return f"A dívida é {self.nome}"