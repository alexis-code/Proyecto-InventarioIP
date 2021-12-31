from django.db import models
from django.db.models.deletion import PROTECT

class Direccionip(models.Model):
    id_direccionPK = models.AutoField(primary_key=True)
    direccion = models.CharField('Ingrese la dirección IP',max_length=15,unique=True,blank=False,default="Sin asignar")
    descripcion = models.TextField('Descripción',blank=True,default="sin descripción")
    estado = models.IntegerField(null=True,default=0)

    def __str__(self) -> str:
        return self.direccion

    class Meta:
        ordering = ['id_direccionPK']
        verbose_name = "Direccion"
        verbose_name_plural = "Direccion"
        db_table  = "tb_direccionip"
