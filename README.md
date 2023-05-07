// Crear un entorno virtual:

python3 -m venv venv


// Activar el entorno virtual

.\env\Scripts\activate

// instalar Mysql y Pymysql wheel

 pip install mysqlclient pymysql wheel pillow


// video tutorial

https://www.youtube.com/watch?v=TNtrAvNNxTY

// Instalar Django en el env

pip install Django==4.1.1

// Crear proyecto Django 

django-admin startproject frontend

// Entrar a la carpeta del proyecto

cd frontend

//Crear Aplicacion

django-admin startapp core

// En settings se debe agregar la aplicacion y los datos de la base de datos

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
        'NAME':'fovis',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
// Registrar core en admin.py

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Usuarios
# Register your models here.
admin.site.register(Usuarios)


// Crear modelo en core



    ejemplo: 
    nombre=models.CharField(max_length=255, blank=True)
    apellido=models.CharField(max_length=255, blank=True)
    cedula=models.CharField(max_length=255)


from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Usuarios
# Register your models here.
admin.site.register(Usuarios)

##//hacer la Migracion del modelo

python manage.py makemigrations

// migrar los datos del model a la base de datos

python manage.py migrate

// crear un super usuario

python manage.py createsuperuser

//hacer la Migracion del modelo

python manage.py makemigrations

//ejecutar el servidor Django

python manage.py runserver


// Crear vista basada en class (tambien se puede vista basada en funciones) 

// crear archivo urls.py en la carpeta api
 ejemplo:
 from django.urls import path
from .views import UsuariosView


urlpatterns=[
    path('usuarios/', UsuariosView.as_view())
]

registrar en el proyecto las urls


// tener en cuenta csrf
El CSRF (del inglés Cross-site request forgery o falsificación de petición en sitios cruzados) es un tipo de exploit malicioso de un sitio web en el que comandos no autorizados son transmitidos por un usuario en el cual el sitio web confía.1​ Esta vulnerabilidad es conocida también por otros nombres como XSRF, enlace hostil, ataque de un clic, secuestro de sesión, y ataque automático.

//Desplegar

Pasos para llevar su aplicación Django desde el desarrollo hasta la producción

abra la carpeta de su proyecto y luego busque settings.py busque la siguiente línea,

ADVERTENCIA DE SEGURIDAD: ¡no ejecute con la depuración activada en producción!
DEPURAR = Falso

Cambie la depuración a falso.

Cambie sus credenciales de base de datos con las credenciales de base de datos del servidor de producción real en su configuración.py

BASES DE DATOS = { 'predeterminado': { 'MOTOR': 'django.db.backends.mysql', 'NOMBRE': 'seocrawler', 'USUARIO': '', 'CONTRASEÑA': '', 'HOST': 'localhost ', 'PUERTO': '' } }

una vez hecho, suba la carpeta de su proyecto a la carpeta en el servidor

open putty ingrese las credenciales de su servidor, luego aparecerá una terminal o cmd.

verifique que Python esté instalado en su servidor ejecutando el siguiente comando en la terminal python -V

luego verifique si django está instalado ejecutando django-admin --version, asegúrese de que la versión de django que usó para desarrollar el proyecto coincida con la del servidor si no instala la versión específica.

ahora usando el comando cd para ir a la carpeta del proyecto que contiene el archivo manage.py.

ahora ejecute python manage.py showmigrations, esto mostrará si alguna migración de base de datos está pendiente para su proyecto.

ahora ejecute python manage.py makemigrations, esto migrará las tablas de db a la base de datos del servidor de producción.

ahora ejecute python manage.py runserver 0.0.0.0:8000 y luego vaya a su dominio como www.example.com:8000 en el navegador, para probar si su sitio está funcionando.

Una vez que su sitio esté activo y en funcionamiento, queremos que el comando python manage.py runserver se ejecute incluso después de que la terminal esté cerrada (es decir, el comando python manage.py runserver como tarea/proceso en segundo plano).

para hacer eso, ejecute nohup python manage.py runserver y esto ejecutará el comando en segundo plano y nunca terminará el proceso, incluso cuando la terminal Putty esté cerrada.




//Lanzar a git hub

https://www.javatpoint.com/django-deploy-on-github


//hacer visible la plataforma localmente

https://stackoverflow.com/questions/5524116/accessing-localhost-xampp-from-another-computer-over-lan-network-how-to