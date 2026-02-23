from django.db import models

class Fixos(models.Model):
    categoria_escolha = [
        ('Moradia', 'Moradia'),
        ('Contas', 'Contas'),
        ('Saúde', 'Saúde'),
        ('Assinaturas', 'Assinaturas'),
        ('Educação', 'Educação'),
        ('Transporte', 'Transporte'),
    ]

    nome = models.CharField(max_length=100)
    data = models.DateField()
    categoria = models.CharField(choices=categoria_escolha, default='Assinatura', max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"O fixo é {self.nome}"