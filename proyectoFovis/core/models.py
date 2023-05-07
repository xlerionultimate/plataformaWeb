from django.db import models
from django.contrib.auth.models import User



class Categoria(models.Model):
    name = models.CharField(verbose_name='Categoria', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
class Geografica(models.Model):
    name = models.CharField(verbose_name='Geografica', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Geografica'
        verbose_name_plural = 'Geograficas'
        
class Parentesco(models.Model):
    name = models.CharField(verbose_name='Parentesco', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Parentesco'
        verbose_name_plural = 'Parentescos'
        
class EstadoCivil(models.Model):
    name = models.CharField(verbose_name='Estado Civil', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Estado Civil'
        
class Sexo(models.Model):
    name = models.CharField(verbose_name='Sexo', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
        
class NivelEscolaridad(models.Model):
    name = models.CharField(verbose_name='Nivel Escolaridad', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'
        
class Ocupacion(models.Model):
    name = models.CharField(verbose_name='Ocupación', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ocupación'
        verbose_name_plural = 'Ocupaciones'
        
class TipologiaFamiliar(models.Model):
    name = models.CharField(verbose_name='Tipología Familiar', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tipologia Familiar'
        verbose_name_plural = 'Tipologia Familiares'
        

        
class TiempoViviendo(models.Model):
    name = models.CharField(verbose_name='Tiempo viviendo en el Municipio', max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tiempo viviendo'
        
class LugarProcedencia(models.Model):
    name = models.CharField(verbose_name='Lugar de procedencia del Grupo Familiar', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Procedencia'
        verbose_name_plural = 'Procedencias'
        
class SituacionLaboral(models.Model):
    name = models.CharField(verbose_name='Situación laboral del Jefe de Hogar', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Situación laboral'
        verbose_name_plural = 'Situaciones Laborales'
        
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Actividad Económica'
        verbose_name_plural = 'Actividades Económicas'
        
class TrabajoEsporadico(models.Model):
    name = models.CharField(verbose_name='Trabaja Esporádicamente?', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Trabajo Esporádico'
        verbose_name_plural = 'Trabajos Esporádicos'


class IngresosTotalesFamiliares(models.Model):
    name = models.CharField(verbose_name='Ingresos totales', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ingreso Total Familiar'
        verbose_name_plural = 'Ingresos totales Familiares'
        
        
class SistemaSalud(models.Model):
    name = models.CharField(verbose_name='Tipo de sistema de Salud?', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tipo de Sistema de Salud'
        verbose_name_plural = 'Tipos de Sistemas de Salud'
        
class CompensacionFamiliar(models.Model):
    name = models.CharField(verbose_name='Afiliado al Sistema de Compensación Familiar?', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Afiliado a la Caja de Compensación'
        verbose_name_plural = 'Afiliados a la Caja de Compensaciónes'
        
        
class Pensiones(models.Model):
    name = models.CharField(verbose_name='Algún integrante hace aportes al sistema de pensiones?', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Algún integrante hace aportes al sistema de pensiones'
        verbose_name_plural = 'Algunos integrantes hacen aportes al sistema de pensiones'
        
        
class Discapacidad(models.Model):
    name = models.CharField(verbose_name='Existen personas con Discapacidad en el grupo Familiar?', max_length=90, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Persona con Discapacidad'
        verbose_name_plural = 'Personas con Discapacidad'
        
        
# Create your models here.


class Formulario(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP',null= True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name= ("Seleccione la Categoria a la que pertenece"))
    resolucion_numero=models.CharField(verbose_name='Codigo de la Resolución',max_length=100, blank=False)
    resolucion_pdf = models.FileField(verbose_name='Agregar Archivo de Resolución', null=True, upload_to='resoluciones', blank=False)
    fecha = models.DateField(verbose_name='Fecha de Realización', auto_now_add=True, unique=True)
    ficha=models.CharField(verbose_name='Ficha N°',max_length=100, blank=False, unique=True)
    responsable=models.CharField(verbose_name='Profesional Responsable',max_length=100, blank=False)
    nombre_suministro_de_informacion=models.CharField(verbose_name='Nombre de quien suministra la Información',max_length=100, blank=False)
    apellido_suministro_de_informacion=models.CharField(verbose_name='Apellido de quien suministra la Información',max_length=100, blank=False)
    cedula_suministro_de_informacion=models.CharField(verbose_name='Cédula de suministrante de la información',max_length=100, blank=True)
    lugar_expedicion_informacion=models.CharField(verbose_name='Lugar de Expedición de la Cédula del que suministra la Información', max_length=100, blank=False)
    parentesco_suministro_de_informacion=models.CharField(verbose_name='Parentesco con el Jefe de Hogar',max_length=100, blank=False, editable=True)
    ubicacion_geografica=models.ForeignKey(Geografica, on_delete=models.CASCADE, verbose_name= ("Seleccione su tipo de residencia"))
    municipio=models.CharField(verbose_name='Municipio',max_length=100, blank=False, editable=True)
    direccion_municipio=models.CharField(verbose_name='Direccion de Municipio',max_length=100, blank=False, editable=True)
    telefono_municipio=models.CharField(verbose_name='Teléfono Del suministrante de la información',max_length=100, blank=True)
    corregimiento=models.CharField(verbose_name='Corregimiento', max_length=100, blank=True)
    nombre_jefe_hogar=models.CharField(verbose_name='Nombre del Jefe de Hogar',max_length=100, blank=False)
    cedula_jefe_hogar=models.CharField(verbose_name='Cédula de Jefe de Hogar',max_length=100, blank=True)
    lugar_expedicion_cedula_jefe=models.CharField(verbose_name='Lugar de Expedición de la Cédula',max_length=100, blank=False)
    nombre_conyugue=models.CharField(verbose_name='Nombre del conyugue',max_length=100, blank=True)
    cedula_conyugue=models.CharField(verbose_name='Cédula del conyugue',max_length=100, blank=True)
    lugar_expedicion_conyugue=models.CharField(verbose_name='Lugar de Expedición de la Cédula',max_length=100, blank=False)
    composicion_familiar_nom_ape=models.CharField(verbose_name='Nombres Jefe de Hogar',max_length=100, blank=True)
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE, verbose_name= 'Parentesco con el Jefe de Hogar')
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, verbose_name= 'Estado Civil')
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, verbose_name= 'Sexo')
    edad= models.CharField(verbose_name='Edad',max_length=100, blank=False, unique=False)
    nivel_escolaridad = models.ForeignKey(NivelEscolaridad, on_delete=models.CASCADE, verbose_name= 'Nivel de Escolaridad')
    ocupacion = models.TextField(verbose_name='Ocupación', max_length=600, blank=True)
    tipologia_familar = models.ForeignKey(TipologiaFamiliar, on_delete=models.CASCADE, verbose_name= 'Tipologia Familiar')
    tipologia_familiar_otra= models.TextField(verbose_name='Otra Tipología', max_length=600, blank=True)
    numero_hogares_en_vivienda = models.CharField(verbose_name='Numero de viviendas en el Hogar',max_length=100, blank=True)
    arraigo_tiempo_viviendo = models.ForeignKey(TiempoViviendo, on_delete=models.CASCADE, verbose_name= 'Tiempo que lleva viviendo en el Municipio')
    arraigo_lugar_procedencia_familiar = models.ForeignKey(LugarProcedencia, on_delete=models.CASCADE, verbose_name= 'Lugar de Procedencia del grupo Familiar')
    arraigo_lugar_de_procedencia_tiempo = models.IntegerField(verbose_name= "Sí contesto mas de 16 años, Cuántos Años lleva en el municipio?", default=0, null=True, blank=True)
    tiempo_residencia_municipio=models.IntegerField(verbose_name= 'Hace cuántos? años reside en el Municipio', default=0, null=True, blank=False)
    aspecto_economico_familiar=models.ForeignKey(SituacionLaboral, on_delete=models.CASCADE, verbose_name= 'Situación laboral del Jefe de Hogar')
    actividad_economica=models.CharField(verbose_name='Cuál es su Actividad Económica',max_length=100, blank=True)
    nombre_empresa=models.CharField(verbose_name='Nombre de la Empresa',max_length=100, blank=True)
    telefono_empresa=models.CharField(verbose_name='Teléfono de la Empresa',max_length=100, blank=True)
    trabajo_esporadico=models.ForeignKey(TrabajoEsporadico, on_delete=models.CASCADE,  blank=True, verbose_name= 'Trabajo Esporadico?')
    trabajo_esporadico_actividad=models.CharField(verbose_name='En qué Actividad?',max_length=100, blank=True)
    desempleado_tiempo=models.CharField(verbose_name='Hace Cuánto esta Desempleado?',max_length=100, blank=True)
    conyugue_trabaja=models.CharField(verbose_name='Su Conyugue Trabaja?',max_length=100, blank=True)
    trabaja_conyugue=models.CharField(verbose_name='Su Conyugue Trabaja?2',max_length=100, blank=True)
    conyugue_tiempo_trabajo=models.CharField(verbose_name='Quién o Quiénes?',max_length=100, blank=True)
    nombre_empresa_conyugue=models.CharField(verbose_name='Nombre de la Empresa',max_length=100, blank=True)
    telefono_empresa_conyugue=models.CharField(verbose_name='Teléfono de la Empresa donde trabaja su conyugue',max_length=100, blank=True)
    ingresos_familaires_totales=models.ForeignKey(IngresosTotalesFamiliares, on_delete=models.CASCADE, verbose_name= 'Ingresos Totales Familiares')
    personas_a_cargo_jefe_hogar= models.CharField(verbose_name='Perosnas a cargo del jefe de familia',max_length=100, blank=True)
    sistema_de_salud=models.ForeignKey(SistemaSalud, on_delete=models.CASCADE, verbose_name= 'Qué tipo de sistema de Salud tiene la Familia?')
    caja_de_compensación_familiar=models.ForeignKey(CompensacionFamiliar, on_delete=models.CASCADE, verbose_name= 'Alguno de los Miembros hace Aportes al sistema de Salud?')
    cual_caja_compensaciones=models.CharField(verbose_name='Cuál Caja?',max_length=100, blank=True)
    sistema_pensiones=models.ForeignKey(Pensiones, on_delete=models.CASCADE, verbose_name= 'Algún integrante hace aportes al sistema de pensiones?')
    discapacidad_familiar=models.ForeignKey(Discapacidad, on_delete=models.CASCADE, blank=True, verbose_name= 'Existen Personas dentro de la Familia con Discapacidad?')
    cuantas_discapacidad_familia= models.CharField(verbose_name='Cuántas Personas?',max_length=10, blank=True)
    tipo_discapacidad=models.CharField(verbose_name='Qué tipo de discapacidad?',max_length=100, blank=True, null=True)
    observaciones=models.TextField(verbose_name='Observaciones', max_length=100, blank=True)
    imagen_firma = models.ImageField(verbose_name='Agregar Imagen de la Firma', null=True, upload_to='firma',blank=False)
    planos = models.ImageField(verbose_name='Agregar Planos', null=True, upload_to='planos',blank=True)
    
    
    
    def __str__(self):
        return (self.nombre_suministro_de_informacion)
    class Meta:
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'