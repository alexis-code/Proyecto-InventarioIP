from django.db import models

class Agencia(models.Model):
    id_agenciaPK = models.AutoField(primary_key=True)
    codigo = models.CharField('Código de Agencia',unique=True,max_length=10,blank=False,default="s/c")
    nombre = models.CharField('Nombre de Agencia',unique=True,max_length=30,blank=False,default="s/n")
    descripcion = models.TextField('Descripción',blank=True,default="sin descripción")

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        ordering = ['-id_agenciaPK']
        verbose_name = 'Agencia'
        verbose_name_plural = 'Agencia'
        db_table = 'tb_agencia'
