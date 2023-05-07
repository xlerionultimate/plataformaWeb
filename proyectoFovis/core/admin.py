from django.contrib import admin
from .models import Categoria
from .models import Geografica
from .models import Parentesco
from .models import EstadoCivil
from .models import Sexo
from .models import NivelEscolaridad
from .models import TipologiaFamiliar
from .models import TiempoViviendo
from .models import LugarProcedencia
from .models import SituacionLaboral
from .models import TrabajoEsporadico
from .models import IngresosTotalesFamiliares
from .models import SistemaSalud
from .models import CompensacionFamiliar
from .models import Pensiones
from .models import Discapacidad
from .models import Formulario

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Geografica)
admin.site.register(Parentesco)
admin.site.register(EstadoCivil)
admin.site.register(Sexo)
admin.site.register(NivelEscolaridad)
admin.site.register(TipologiaFamiliar)
admin.site.register(TiempoViviendo)
admin.site.register(LugarProcedencia)
admin.site.register(SituacionLaboral)
admin.site.register(TrabajoEsporadico)
admin.site.register(IngresosTotalesFamiliares)
admin.site.register(SistemaSalud)
admin.site.register(CompensacionFamiliar)
admin.site.register(Pensiones)
admin.site.register(Discapacidad)

#admin.site.register(Formulario)

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display =('ficha','fecha','categoria','nombre_suministro_de_informacion', 
                   'apellido_suministro_de_informacion' ,'responsable',
                   'cedula_suministro_de_informacion','lugar_expedicion_informacion','telefono_municipio',
                   'resolucion_numero', 'parentesco_suministro_de_informacion', 'municipio',
                   'corregimiento','nombre_jefe_hogar', 'edad', 'cual_caja_compensaciones',
                   
                   )
    
    
    
    ordering = ('categoria', )
    
    
    
    
    search_fields = ('nombre_suministro_de_informacion', 
                     'ficha','fecha','responsable',
                     'cedula_suministro_de_informacion',
                   'cedula_suministro_de_informacion','lugar_expedicion_informacion',
                     'resolucion_numero','parentesco_suministro_de_informacion','municipio',
                     'corregimiento','nombre_jefe_hogar', 'edad', 'cual_caja_compensaciones',
                     'telefono_municipio',)