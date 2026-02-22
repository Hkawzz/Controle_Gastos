from django.db import models

class Entradas(models.Model):
    data = models.DateField()
    origem = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origem} - {self.valor}"
    
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

class Cartao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    parcela = models.IntegerField()
    categoria = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"A conta do cartão é {self.nome}"

class Caixinhas(models.Model):
    objetivo = models.CharField(max_length=10)
    meta = models.DecimalField(max_digits=10, decimal_places=2)
    guardado = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def falta(self):
        return self.meta - self.guardado
    
    @property
    def processo(self):
        return round((self.guardado / self.meta) * 100, 2)

    def __str__(self):
        return f"O objetivo é {self.objetivo}"
    
class Dividas(models.Model):
    nome = models.CharField(max_length=100)
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    total_parcela = models.IntegerField()
    data = models.DateField()

    @property
    def total(self):
        return self.total_parcela * self.valor_parcela

    def __str__(self):
        return f"A dívida é {self.nome}"