from django.db import models

# Create your models here.
class leccion(models.Model):
    idLeccion = models.IntegerField(primary_key=True)
    nombreLeccion = models.CharField(max_length=100)
    texto = models.CharField(max_length=800)
    imagen = models.FileField()


    def _str_(self):
        return self.nombreLeccion 