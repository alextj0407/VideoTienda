# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'actor'
    
    def __str__(self):
        return self.nombre

class ActorHasVideo(models.Model):
    actor_id = models.IntegerField(db_column='Actor_id', primary_key=True)  # Field name made lowercase.
    video_id = models.IntegerField(db_column='Video_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actor_has_video'
        unique_together = (('actor_id', 'video_id'),)

    def __str__(self):
        return self.actor_id


class Alquiler(models.Model):
    fecha_alquiler = models.DateField()
    fecha_devolucion = models.DateField()
    dias_retrazo = models.IntegerField()
    video_id = models.IntegerField(db_column='Video_id')  # Field name made lowercase.
    video_director_id = models.IntegerField(db_column='Video_Director_id')  # Field name made lowercase.
    video_formato_id = models.IntegerField(db_column='Video_Formato_id')  # Field name made lowercase.
    cliente_id = models.IntegerField(db_column='Cliente_id')  # Field name made lowercase.
    listado_id = models.IntegerField(db_column='Listado_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alquiler'
        unique_together = (('id', 'video_id', 'video_director_id', 'video_formato_id', 'cliente_id', 'listado_id'),)

    def __str__(self):
        return 'Video '+str(self.video_id) +' Cliente'+ str(self.cliente_id)

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    direccion = models.CharField(max_length=15)
    codigo = models.CharField(unique=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.nombre

class Director(models.Model):
    nombre = models.CharField(max_length=45)
    nacionalidad = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'director'

    def __str__(self):
        return self.nombre

class Formato(models.Model):
    nombre = models.CharField(max_length=45)
    valor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'formato'

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'genero'
    def __str__(self):
        return self.nombre

class Listado(models.Model):
    tipo = models.CharField(max_length=15)
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'listado'

    def __str__(self):
        return self.tipo

class Video(models.Model):
    codigo = models.CharField(unique=True, max_length=10)
    titulo = models.CharField(max_length=15)
    idioma = models.CharField(max_length=15)
    duracion = models.TimeField()
    director_id = models.IntegerField(db_column='Director_id')  # Field name made lowercase.
    formato_id = models.IntegerField(db_column='Formato_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'video'
        unique_together = (('id', 'director_id', 'formato_id'),)

    def __str__(self):
        return self.titulo

class VideoHasGenero(models.Model):
    video_id = models.IntegerField(db_column='Video_id', primary_key=True)  # Field name made lowercase.
    genero_id = models.IntegerField(db_column='Genero_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'video_has_genero'
        unique_together = (('video_id', 'genero_id'),)

    def __str__(self):
        return str(self.video_id) +' '+ str(self.genero_id)