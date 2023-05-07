from django.contrib import admin
from django.urls import path
from appFovis import views
from appFovis.views import IndexView
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('index/', IndexView.as_view(), name='index'),
    path('formulario_busqueda/', views.formulario_busqueda, name='formulario-busqueda'),
    path('add_formulario/', views.add_formulario, name='add-formulario'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)