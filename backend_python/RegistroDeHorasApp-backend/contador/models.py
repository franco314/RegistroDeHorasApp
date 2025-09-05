from django.db import models
from django.contrib.auth.models import User

class RegistroDeHoras(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registros_horas')
    fecha = models.DateField()
    horas = models.DecimalField(max_digits=3, decimal_places=1)  # Para poder registrar hasta 99.9 horas, por ejemplo

    def __str__(self):
        return f"{self.usuario.username} - {self.fecha} - {self.horas} hs"
