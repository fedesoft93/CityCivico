from django.db import models

# Create your models here.
class usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    nombreUsuario = models.CharField(max_length=100)
    apellidoUsuario = models.CharField(max_length=100)
    direccionUsuario = models.CharField(max_length=100)
    telefonoUsuario = models.IntegerField()
    emailUsuario = models.CharField(max_length=100)

    def _str_(self):
        return self.nombreUsuario 
        