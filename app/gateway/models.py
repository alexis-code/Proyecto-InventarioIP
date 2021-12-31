from django.db import models
from django.db.models.fields import CharField

class Gateway(models.Model):
    id_gatewayPK = models.AutoField(primary_key=True)
    direccion = models.CharField('Puerta de Enlace',blank=False, max_length=15,default="s/p", unique=True)
    descripcion = models.TextField('Descripción',blank=True,default="Sin Descripción")

    def __str__(self) -> str:
        return self.direccion
    
    class Meta:
        ordering=['-id_gatewayPK']
        verbose_name = "Gateway"
        verbose_name_plural = "Gateway"
        db_table = 'tb_gateway'