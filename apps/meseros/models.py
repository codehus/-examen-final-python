from django.db import models

# Create your models here.
class Meseros(models.Model):
    pais = models.CharField(max_length=50,default='Perú')
    edad = models.IntegerField(default=0)

    def __str__(self):
        return f"Mesero de {self.edad} años, y es de {self.pais}"


