from django.db import models

# Create your models here.
class denuncia(models.Model):
    idDenuncia = models.AutoField(primary_key=True)
    idTipoDenuncia = models.IntegerField()
    asuntoDenuncia = models.CharField(max_length=100)
    descripcionDenuncia = models.CharField(max_length=300)
    evidenciaDenuncia = models.FileField()
    ubicacionDeuncia = models.CharField(max_length=100)
    idEstadoDenuncia = models.IntegerField()


    def _str_(self):
        return self.asuntoDenuncia 