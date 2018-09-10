from django.db import models

# Create your models here.
class estadoDenuncia(models.Model):
    idEstadoDenuncia = models.AutoField(primary_key=True)
    estadoDenuncia = models.CharField(max_length=100)

    def _str_(self):
        return self.estadoDenuncia 