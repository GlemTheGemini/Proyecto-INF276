from django.db import models


class Reserva(models.Model):
    bloque = models.CharField(max_length=10)

    def __str__(self):
        return f'Bloque {self.bloque}'
