from django.db import models

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