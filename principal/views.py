from django.shortcuts import render
from principal.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages 

# Create your views here.
def Home(request):
    
    return render (request, "index.html")

def Parametros (request):
    return render (request, "crud/index.html")  

def Login(request):
    return render (request, "login.html")


 #-----------------------------------Ciudad-----------------------------------------------------#
class ListadoCiudad(CreateView,ListView,SuccessMessageMixin):

    model = Ciudad
    form = Ciudad
    fields = "__all__"
    
    success_message ='Ciudad creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer' 
    
class CiudadDetalle (DetailView):
    model =Ciudad

class CiudadActualizar(SuccessMessageMixin,UpdateView):
    model =Ciudad
    form = Ciudad
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Ciudad' de nuestra Base de Datos 
    success_message = 'Ciudad Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer') # Redireccionamos a la vista principal 'leer'
    
class CiudadEliminar(SuccessMessageMixin, DeleteView): 
    model = Ciudad
    form = Ciudad
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Ciudad Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer'
    
    #-----------------------------------Ciudad-----------------------------------------------------#
    #-----------------------------------Genero-----------------------------------------------------#
class ListadoGenero(CreateView,ListView,SuccessMessageMixin):

    model = Genero
    form = Genero
    fields = "__all__"
    
    success_message ='Genero creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerge') # Redireccionamos a la vista principal 'leer' 
    
class GeneroDetalle (DetailView):
    model =Genero

class GeneroActualizar(SuccessMessageMixin,UpdateView):
    model =Genero
    form = Genero
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Genero' de nuestra Base de Datos 
    success_message = 'Genero Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerge') # Redireccionamos a la vista principal 'leer'
    
class GeneroEliminar(SuccessMessageMixin, DeleteView): 
    model = Genero
    form = Genero
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Genero Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerge') # Redireccionamos a la vista principal 'leer'
    
    #-----------------------------------Genero-----------------------------------------------------#
     #-----------------------------------Informeubicación-----------------------------------------------------#
class ListadoInformeubicación(CreateView,ListView,SuccessMessageMixin):

    model = Informeubicación
    form = Informeubicación
    fields = "__all__"
    
    success_message ='Informeubicación creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerge') # Redireccionamos a la vista principal 'leer' 
    
class InformeubicaciónDetalle (DetailView):
    model =Informeubicación

class InformeubicaciónActualizar(SuccessMessageMixin,UpdateView):
    model =Informeubicación
    form = Informeubicación
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Informeubicación' de nuestra Base de Datos 
    success_message = 'Informeubicación Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerge') # Redireccionamos a la vista principal 'leer'
    
class InformeubicaciónEliminar(SuccessMessageMixin, DeleteView): 
    model = Informeubicación
    form = Informeubicación
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Informeubicación Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerge') # Redireccionamos a la vista principal 'leer'
    
    #-----------------------------------Informeubicación-----------------------------------------------------#
    #-----------------------------------Parqueadero-----------------------------------------------------#
class ListadoParqueadero(CreateView,ListView,SuccessMessageMixin):

    model = Parqueadero
    form = Parqueadero
    fields = "__all__"
    
    success_message ='Parqueadero creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerge') # Redireccionamos a la vista principal 'leer' 
    
class ParqueaderoDetalle (DetailView):
    model =Parqueadero

class ParqueaderoActualizar(SuccessMessageMixin,UpdateView):
    model =Parqueadero
    form = Parqueadero
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Parqueadero' de nuestra Base de Datos 
    success_message = 'Parqueadero Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerge') # Redireccionamos a la vista principal 'leer'
    
class ParqueaderoEliminar(SuccessMessageMixin, DeleteView): 
    model = Parqueadero
    form = Parqueadero
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Parqueadero Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerge') # Redireccionamos a la vista principal 'leer'
    
    #-----------------------------------Parqueadero-----------------------------------------------------#
    

   