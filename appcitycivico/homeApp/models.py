from django.db import models

# Create your models here.
class homeApp(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    idLeccion = models.IntegerField()
    idDenuncia = models.IntegerField()
    

    def _str_(self):
        return self.idUsuario 