from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length = 255, blank = True, null = True)
    apellido_paterno = models.CharField(max_length = 255, blank = True, null = True)
    apellido_materno = models.CharField(max_length = 255, blank = True, null = True)
    dni = models.CharField(max_length = 255, blank = True, null = True)

    def __str__(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombre)