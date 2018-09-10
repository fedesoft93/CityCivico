from django.db import models

# Create your models here.
class tipoDenuncia(models.Model):
    idTipoDenuncia = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=100)

    def _str_(self):
        return self.tipo