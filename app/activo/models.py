from django.db import models
from django.db.models.deletion import PROTECT

from ..agencia.models import Agencia
from ..categoria.models import Categoria
from ..direccionip.models import Direccionip
from ..gateway.models import Gateway

class Activo(models.Model):
    id_activoPK = models.AutoField(primary_key=True)
    id_agenciaFK = models.ForeignKey(Agencia,on_delete=PROTECT)
    id_categoriaFK = models.ForeignKey(Categoria,on_delete=PROTECT)
    id_direccionipFK = models.OneToOneField(Direccionip,on_delete=PROTECT)
    id_gatewayFK = models.ForeignKey(Gateway,on_delete=PROTECT)
    nombre = models.CharField('Nombre del Activo',unique=True,max_length=150,blank=False,default="s/n")
    descripcion = models.TextField('Descripción del Activo',blank=True,default="sin descripcion")

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        ordering = ['id_agenciaFK']
        verbose_name = "Activo"
        verbose_name_plural = "Activo"
        db_table = "tb_activo"