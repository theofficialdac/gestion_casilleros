from django.db import models

class Casillero(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    ubicacion = models.CharField(max_length=100)
    ocupado = models.BooleanField(default=False)

    def __str__(self):
        return f'Casillero {self.numero} - {self.ubicacion}'

class Arrendatario(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=12, unique=True)
    celular = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Contrato(models.Model):
    casillero = models.ForeignKey(Casillero, on_delete=models.CASCADE)
    arrendatario = models.ForeignKey(Arrendatario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f'Contrato {self.id} para {self.casillero}'
