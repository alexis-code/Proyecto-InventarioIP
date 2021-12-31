from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from django.utils import tree

class Categoria(models.Model):
    id_categoriaPK = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria',unique=True,max_length=50, blank=False,default="sin nombre")
    descripcion = models.TextField('Descripción', blank=True,default="sin descripcion")

    def __str__(self) -> str:
        return self.nombre

    class Meta: 
        ordering = ['-id_categoriaPK']
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria"
        db_table = "tb_categoria"
