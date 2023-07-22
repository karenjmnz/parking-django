
from django.urls import path
from .views import *


urlpatterns = [
    
path('parametros/',Parametros, name='leerpar'),





#--------------------------------------------URL ciudad ------------------------------------------------------------------------#
    
path('Ciudad/', ListadoCiudad.as_view(template_name = "crud/Ciudad/tables.html"), name='leerre'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
path('Ciudad/detalle/<int:pk>', CiudadDetalle.as_view(template_name = "crud/Ciudad/detalle.html"), name='detallesre'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Ciudad/editar/<int:pk>', CiudadActualizar.as_view(template_name = "crud/Ciudad/actualizar.html"), name='actualizarre'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Ciudad/eliminar/<int:pk>', CiudadEliminar.as_view(), name='crud/Ciudad/eliminar.html'),     
 #--------------------------------------------URL Ciudad ------------------------------------------------------------------------#
 #--------------------------------------------URL ciudad ------------------------------------------------------------------------#
    
path('Genero/', ListadoGenero.as_view(template_name = "crud/Genero/tables.html"), name='leerge'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
path('Genero/detalle/<int:pk>', GeneroDetalle.as_view(template_name = "crud/Genero/detalle.html"), name='detallesge'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Genero/editar/<int:pk>', GeneroActualizar.as_view(template_name = "crud/Genero/actualizar.html"), name='actualizarge'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Genero/eliminar/<int:pk>', GeneroEliminar.as_view(), name='crud/Genero/eliminar.html'),     
 #--------------------------------------------URL Ciudad ------------------------------------------------------------------------#
   #--------------------------------------------URL ciudad ------------------------------------------------------------------------#
    
path('Informeubicación/', ListadoInformeubicación.as_view(template_name = "crud/Informeubicación/tables.html"), name='leerge'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
path('Informeubicación/detalle/<int:pk>', InformeubicaciónDetalle.as_view(template_name = "crud/Informeubicación/detalle.html"), name='detallesge'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Informeubicación/editar/<int:pk>', InformeubicaciónActualizar.as_view(template_name = "crud/Informeubicación/actualizar.html"), name='actualizarge'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Informeubicación/eliminar/<int:pk>', InformeubicaciónEliminar.as_view(), name='crud/Informeubicación/eliminar.html'),     
 #--------------------------------------------URL Ciudad ------------------------------------------------------------------------#
   #--------------------------------------------URL ciudad ------------------------------------------------------------------------#
    
path('Parqueadero/', ListadoParqueadero.as_view(template_name = "crud/Parqueadero/tables.html"), name='leerge'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
path('Parqueadero/detalle/<int:pk>', ParqueaderoDetalle.as_view(template_name = "crud/Parqueadero/detalle.html"), name='detallesge'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Parqueadero/editar/<int:pk>', ParqueaderoActualizar.as_view(template_name = "crud/Parqueadero/actualizar.html"), name='actualizarge'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Parqueadero/eliminar/<int:pk>', ParqueaderoEliminar.as_view(), name='crud/Parqueadero/eliminar.html'),     
 #--------------------------------------------URL Ciudad ------------------------------------------------------------------------#
  


]