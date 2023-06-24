from typing import Any
from django import http
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Cliente
import requests
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpRequest
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework import serializers,viewsets
# Create your views here.


class ListarCliente(TemplateView):
    template_name = "base.html"
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        query_dni = request.GET.get("qdni")
        query_apellido = request.GET.get("qapellido")
        criterio_busqueda = {}
        if query_dni or query_apellido:
            if query_dni:
                criterio_busqueda['dni'] = query_dni
            if query_apellido:
                criterio_busqueda['apellido_paterno'] = query_apellido
            kwargs["clientes"] = Cliente.objects.filter(**criterio_busqueda)
        if criterio_busqueda:
            kwargs["clientes"] = Cliente.objects.filter(**criterio_busqueda)
            return super().get(request, *args, **kwargs) 
        api_path = "/apis/cliente"  # Ruta relativa a la API 
        api_url = request.build_absolute_uri(api_path)
        response = requests.get(api_url)
        dictDatos = response.json()
        kwargs["clientes"]=dictDatos
        return super().get(request, *args, **kwargs) 
        
        
    
class CrearCliente(TemplateView):
    template_name = 'modalCliente.html'
    
    def get_context_data(self, **kwargs):
        context = super(CrearCliente, self).get_context_data(**kwargs)
        context['action']= reverse('crear_cliente')
        return context
    
    def post(self, request, *args, **kwargs):
        nombre = request.POST.get("nombre")
        apellido_paterno = request.POST.get("apellidoPaterno")
        apellido_materno = request.POST.get("apellidoMaterno")
        dni = request.POST.get("dni")
        data={
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "dni": dni
        }
        
        
        api_path = "/apis/cliente/"  # Ruta relativa a la API 
        api_url = request.build_absolute_uri(api_path)
        response = requests.post(api_url, json=data)
        print("RESPOSNTE = ", response)
        #response_data = response.json()    
        print("Status Code", response.status_code)
        print("JSON Response ", response.content)
        print("RESPOSE = ",response)
        if response.status_code != 201:
            messages.error(self.request, "Algo Salio Mal...")
        else:
            messages.success(self.request, "Cliente Creado Sastisfactoriamente...")
            
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
class EditarCliente(TemplateView):
    template_name = 'modalCliente.html'
    

    def get_context_data(self, **kwargs):
        context = super(EditarCliente, self).get_context_data(**kwargs)
        idObj = self.kwargs.get('pk', 0)
        api_path = "/apis/cliente/" + str(idObj)   # Ruta relativa a la API 
        api_url = self.request.build_absolute_uri(api_path)
        response = requests.get(api_url)
        dictDatos = response.json()
        print("DATOS EDITAR CLIENTE = ", dictDatos)
        context["cliente"]=dictDatos
        context['action']= reverse('editar_cliente', kwargs = {'pk': idObj})
        return context
    
    def post(self, request, *args, **kwargs):
        idObj = self.kwargs.get('pk', 0)
        nombre = request.POST.get("nombre")
        apellido_paterno = request.POST.get("apellidoPaterno")
        apellido_materno = request.POST.get("apellidoMaterno")
        dni = request.POST.get("dni")
        data={
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "dni": dni
        }
        
        api_path = "/apis/cliente/" + str(idObj) + "/"   # Ruta relativa a la API 
        api_url = request.build_absolute_uri(api_path)
        response = requests.put(api_url, json=data)
        print("RESPOSNTE = ", response)
        #response_data = response.json()    
        print("Status Code", response.status_code)
        if response.status_code != 200:
            messages.error(self.request, "Algo Salio Mal...")
        else:
            messages.success(self.request, "Cliente Editado Sastisfactoriamente...")
        print("JSON Response ", response.content)
        print("RESPOSE = ",response)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
class EliminarCliente(TemplateView):
    template_name = 'modalEliminarCliente.html'
    

    def get_context_data(self, **kwargs):
        context = super(EliminarCliente, self).get_context_data(**kwargs)
        idObj = self.kwargs.get('pk', 0)
        api_path = "/apis/cliente/" + str(idObj)   # Ruta relativa a la API 
        api_url = self.request.build_absolute_uri(api_path)
        response = requests.get(api_url)
        dictDatos = response.json()
        print("DATOS EDITAR CLIENTE = ", dictDatos)
        context["cliente"]=dictDatos
        context['action']= reverse('eliminar_cliente', kwargs = {'pk': idObj})
        return context
    
    def post(self, request, *args, **kwargs):
        idObj = self.kwargs.get('pk', 0)
        nombre = request.POST.get("nombre")
        apellido_paterno = request.POST.get("apellidoPaterno")
        apellido_materno = request.POST.get("apellidoMaterno")
        dni = request.POST.get("dni")
        data={
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "dni": dni
        }
        
        api_path = "/apis/cliente/" + str(idObj) + "/"   # Ruta relativa a la API 
        api_url = request.build_absolute_uri(api_path)
        response = requests.delete(api_url, json=data)
        print("RESPOSNTE = ", response)
        #response_data = response.json()    
        print("Status Code", response.status_code)
        print("JSON Response ", response.content)
        print("RESPOSE = ",response)
        if response.status_code != 204:
            messages.error(self.request, "Algo Salio Mal...")
        else:
            messages.success(self.request, "Cliente Eliminado Sastisfactoriamente...")
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido_paterno', 'apellido_materno', 'dni']

class ClienteApiView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class =  ClienteSerializer
    filter_fields = ['id', 'dni', 'apellido_paterno']


        
        
class CatalogoServicios(TemplateView):
    template_name = "catalogo.html"
    
class About(TemplateView):
    template_name = "about.html"
        