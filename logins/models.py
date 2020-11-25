# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


""" INTEGRACION A LA BASE DE DATOS ORACLE (MODELOS) """

class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombres',max_length=50)
    paterno = models.CharField('Apellido Paterno',max_length=50)
    materno = models.CharField('Apellido Materno',max_length=50)

    class Meta:
        managed = False
        db_table = 'administrador'

    def __str__(self):
        return self.nombre 

class Rubro(models.Model):
    id_rubro = models.AutoField(primary_key=True)
    nom_rubro = models.CharField('nombre',max_length=50)
    class Meta:
        managed = False
        db_table = 'rubro'

    def str(self):
        return 'id rubro '+ str(self.id_rubro)

class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=10)
    direccion = models.CharField(max_length=200)
    nombre = models.CharField(max_length=50)
    rubro = models.ForeignKey(Rubro, models.DO_NOTHING, db_column='rubro')

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return  str(self.id_cliente)

class TipoSolicitud(models.Model):
    id_tiposolicitud = models.AutoField(primary_key=True)
    solicitud = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_solicitud'

    def __str__(self):
        return 'tipo solicitud '+ str(self.id_tiposolicitud)

class EstadoContrato(models.Model):
    id_estado_contrat = models.AutoField(primary_key=True)
    nom_estado_contrato = models.CharField('nombre estado',max_length=50)
    class Meta:
        managed = False
        db_table = 'estado_contrato'

    def str(self):
        return 'Id estado '+ str(self.id_estado_contrat)

class Profesional(models.Model):
    rut_profesional = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    paterno = models.CharField(max_length=50)
    materno = models.CharField(max_length=50, blank=True, null=True)
    estado = models.ForeignKey(EstadoContrato, models.DO_NOTHING, db_column='estado')

    class Meta:
        managed = False
        db_table = 'profesional'
    
    def __str__(self):
        return str(self.rut_profesional)

class SolicitudAsesoria(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_profesional = models.ForeignKey(Profesional, models.DO_NOTHING, db_column='id_profesional')
    tipo_solicitud = models.ForeignKey(TipoSolicitud, models.DO_NOTHING, db_column='tipo_solicitud')
    descripcion_asesoria = models.CharField('Descripcion',max_length=500)

    class Meta:
        managed = False
        db_table = 'solicitud_asesoria'

    def __str__(self):
        return 'Solicitud asesoria '+ str(self.id_solicitud)


class EstadoActividad(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nom_est_actividad = models.CharField('nombre estado',max_length=50)
    class Meta:
        managed = False
        db_table = 'estado_actividad'

    def str(self):
        return 'Id estado actividad '+ str(self.id_estado)

class Asesoria(models.Model):
    id_asesoria = models.AutoField(primary_key=True)
    id_solicitud = models.ForeignKey(SolicitudAsesoria, models.DO_NOTHING, db_column='id_solicitud', unique=True)
    fecha = models.DateField()
    id_estado = models.ForeignKey(EstadoActividad, models.DO_NOTHING, db_column='id_estado', unique=True)
    class Meta:
        managed = False
        db_table = 'asesoria'

    def str(self):
        return 'Asesoria '+ str(self.id_asesoria)

class Capacitacion(models.Model):
    nro_capacitacion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    asistentes = models.CharField(max_length=500)
    id_solicitud = models.ForeignKey(SolicitudAsesoria, models.DO_NOTHING, db_column='id_solicitud')
    descripcion_capa = models.CharField(max_length=500)    
    id_estado = models.ForeignKey(EstadoActividad, models.DO_NOTHING, db_column='id_estado')
    class Meta:
        managed = False
        db_table = 'capacitacion'

    def __str__(self):
        return str(self.nro_capacitacion)


####LOMOVII 
class Checklist(models.Model):
    nro_checklist = models.AutoField(primary_key=True)
    descripcion_check = models.CharField('Descripcion',max_length=50)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_estado = models.ForeignKey(EstadoActividad, models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = False
        db_table = 'checklist'
        
    def __str__(self):
        return 'Checklist '+ str(self.nro_checklist)

class Condicion(models.Model):
    id_condicion = models.AutoField(primary_key=True)
    nom_condicion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'condicion'

    def __str__(self):
        return 'Condicion '+ str(self.id_condicion)

class DetChecklist(models.Model):
    id_detchecklist = models.AutoField(primary_key=True)
    estado = models.CharField('Estado (1-0)',max_length=1)
    checklist_nro_checklist = models.ForeignKey(Checklist, models.DO_NOTHING, db_column='checklist_nro_checklist')
    condicion_id_condicion = models.ForeignKey(Condicion, models.DO_NOTHING, db_column='condicion_id_condicion', unique=True)
    act_mejora = models.CharField('Actividad de mejora',max_length=50)

    class Meta:
        managed = False
        db_table = 'det_checklist'

    def __str__(self):
        return 'Detalle checklist N° '+ str(self.id_detchecklist)




class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class ContratoServicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    id_estado_con = models.ForeignKey(EstadoContrato, models.DO_NOTHING, db_column='id_estado_con')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_profesional = models.ForeignKey(Profesional, models.DO_NOTHING, db_column='id_profesional')

    class Meta:
        managed = False
        db_table = 'contrato_servicio'

    def __str__(self):
        return 'Contrato servicio '+ str(self.id_servicio)

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    pago = models.IntegerField('Monto del pago')
    fecha_pago = models.DateField(blank=True, null=True)
    fecha_vencimiento = models.DateField()
    id_servicio = models.ForeignKey(ContratoServicio, models.DO_NOTHING, db_column='id_servicio')
    total_pagar = models.DateField()

    class Meta:
        managed = False
        db_table = 'pago'

    def __str__(self):
        return  'Pago '+str(self.id_pago) 

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()


    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Visita(models.Model):
    id_visita = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_solicitud = models.ForeignKey(SolicitudAsesoria, models.DO_NOTHING, db_column='id_solicitud')
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    id_estado = models.ForeignKey(EstadoActividad, models.DO_NOTHING, db_column='id_estado')
    nro_checklist = models.ForeignKey(Checklist, models.DO_NOTHING, db_column='nro_checklist')
    
    class Meta:
        managed = False
        db_table = 'visita'

    def __str__(self):
        return 'Visita '+ str(self.id_visita)

class Accidente(models.Model):
    id_accidente = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    fecha = models.DateField()
    id_estado = models.ForeignKey(EstadoActividad, models.DO_NOTHING, db_column='id_estado')


    class Meta:
        managed = False
        db_table = 'accidente'

    def __str__(self):
        return 'Accidente '+ str(self.id_accidente)       



""" --------------------------------------------------------------------- """

