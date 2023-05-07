from django import forms
from django.forms import ModelForm
from core.models import Formulario


class FormularioForm(ModelForm):
    class Meta:
        model = Formulario
        fields = (
                  'id',
                  'categoria',
                  'resolucion_numero',
                  'resolucion_pdf',
                  'ubicacion_geografica',
                  'ficha',
                  'parentesco',
                  'estado_civil',
                  'sexo',
                  'nivel_escolaridad',
                  'tipologia_familar', 
                  'arraigo_tiempo_viviendo',  
                  'arraigo_lugar_procedencia_familiar',   
                  'aspecto_economico_familiar', 
                  'trabajo_esporadico',  
                  'ingresos_familaires_totales',  
                  'sistema_de_salud', 
                  'caja_de_compensación_familiar',
                  'sistema_pensiones',  
                  'discapacidad_familiar',    
                  )
        
        labels = {
            'categoria': '',
            'resolucion_numero': '',
            'resolucion_pdf': '',
            'ubicacion_geografica': '',
            'ficha':'',
            'parentesco': '',
            'estado_civil': '',
            'sexo': '',
            'nivel_escolaridad': '',
            'tipologia_familar': '',
            'arraigo_tiempo_viviendo': '', 
            'arraigo_lugar_procedencia_familiar': '',  
            'aspecto_economico_familiar': '',
            'trabajo_esporadico': '', 
            'ingresos_familaires_totales': '', 
            'sistema_de_salud': '',
            'caja_de_compensación_familiar':'',
            'sistema_pensiones':  '',
            'discapacidad_familiar':'',
        }
        
        widgets = {
            
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Categoria'}),
            'resolucion_numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'N° Resolución'}),
            'resolucion_pdf': forms.FileInput(attrs={ 'type': 'file', 'placeholder':'PDF Resolución'}),
            'ubicacion_geografica': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ubicación Geográfica'}),
            'ficha':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ficha'}),
            'parentesco': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Parentesco con el Jefe de hogar'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Estado Civil'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Sexo'}),
            'nivel_escolaridad': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nivel de escolaridad'}),
            'tipologia_familar': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tipología Familiar'}),
            'arraigo_tiempo_viviendo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Cuantos años lleva residiendo en el municipio?'}), 
            'arraigo_lugar_procedencia_familiar': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Lugar de procedencia familiar'}),  
            'aspecto_economico_familiar': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Situación laboral del jefe de Hogar'}),
            'trabajo_esporadico': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Trabaja esporadicamente?'}), 
            'ingresos_familaires_totales': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Total de ingreso familiar mensual(expresado en pesos)'}), 
            'sistema_de_salud': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Qué tipo de sistema de salud tiene la familia'}),
            'caja_de_compensación_familiar':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Alguno de los miembros estan afiliados a cajas de compensación familiar?'}),
            'sistema_pensiones':  forms.TextInput(attrs={'class': 'form-control', 'placeholder':'algún integrante de la familia hace aportes al sistema de pensiones?'}),
            'discapacidad_familiar':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Existen personas discapacitadasen el grupo familiar?'}),
            
        }
         
        