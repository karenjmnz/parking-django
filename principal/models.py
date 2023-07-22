# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asignacin(models.Model):
    idasignación = models.IntegerField(primary_key=True)
    informeubicación_idinformeubicacion = models.ForeignKey('Informeubicación', models.DO_NOTHING, db_column='informeubicación_idinformeubicación')
    parqueadero = models.ForeignKey('Parqueadero', models.DO_NOTHING)
    registro_idregistro = models.ForeignKey('Registro', models.DO_NOTHING, db_column='registro_idregistro')

    class Meta:
        managed = False
        db_table = 'asignación'


class Ciudad(models.Model):
    idciudad = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Genero(models.Model):
    idgenero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    decripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero'


class Informeubicación(models.Model):
    idinformeubicacion = models.CharField(primary_key=True, max_length=45)
    persona = models.ForeignKey('Persona', models.DO_NOTHING)
    latitud = models.CharField(max_length=45, blank=True, null=True)
    logitud = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informeubicación'


class Parqueadero(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    ubicacion = models.CharField(max_length=45, blank=True, null=True)
    tarifa = models.CharField(max_length=45, blank=True, null=True)
    horario = models.CharField(max_length=45, blank=True, null=True)
    servicio_idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_idservicio')
    tipoparqueadero_idtipoparqueadero = models.ForeignKey('Tipoparqueadero', models.DO_NOTHING, db_column='tipoparqueadero_idtipoparqueadero')

    class Meta:
        managed = False
        db_table = 'parqueadero'


class Persona(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre1 = models.CharField(max_length=45, blank=True, null=True)
    nombre2 = models.CharField(max_length=45, blank=True, null=True)
    apellido1 = models.CharField(max_length=45, blank=True, null=True)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    identificacion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    correoelctronico = models.CharField(max_length=45, blank=True, null=True)
    genero_idgenero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='genero_idgenero')
    tipodepersona = models.ForeignKey('Tipodepersona', models.DO_NOTHING)
    ciudad_idciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_idciudad')
    vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'persona'


class Pqrs(models.Model):
    id = models.IntegerField(primary_key=True)
    asignación_idasignación = models.ForeignKey(Asignacin, models.DO_NOTHING, db_column='asignación_idasignación')

    class Meta:
        managed = False
        db_table = 'pqrs'


class Registro(models.Model):
    idregistro = models.IntegerField(primary_key=True)
    horasalida = models.CharField(max_length=45, blank=True, null=True)
    horaentrada = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro'


class Servicio(models.Model):
    idservicio = models.IntegerField(primary_key=True)
    presentacion = models.CharField(max_length=45, blank=True, null=True)
    stockminimo = models.CharField(max_length=45, blank=True, null=True)
    stockmaximo = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    proveedor = models.CharField(max_length=45, blank=True, null=True)
    tipodeservicio_idtipodeservicio = models.ForeignKey('Tipodeservicio', models.DO_NOTHING, db_column='tipodeservicio_idtipodeservicio')

    class Meta:
        managed = False
        db_table = 'servicio'


class Tipodepersona(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodepersona'
   


class Tipodeservicio(models.Model):
    idtipodeservicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodeservicio'


class Tipodevehiculo(models.Model):
    idtipodevehiculo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodevehiculo'


class Tipoparqueadero(models.Model):
    idtipoparqueadero = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoparqueadero'


class Vehiculo(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    placa = models.CharField(max_length=45, blank=True, null=True)
    tipodevehiculo_idtipodevehiculo = models.ForeignKey(Tipodevehiculo, models.DO_NOTHING, db_column='tipodevehiculo_idtipodevehiculo')

    class Meta:
        managed = False
        db_table = 'vehiculo'
