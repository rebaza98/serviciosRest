"""
URL configuration for serviciosRest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from servicios.views import ListarCliente, ClienteApiView, CatalogoServicios, CrearCliente, EditarCliente, EliminarCliente, About
from rest_framework import routers  

router = routers.DefaultRouter()
router.register('cliente', ClienteApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListarCliente.as_view(), name = 'index'),
    path('crearCliente', CrearCliente.as_view(), name='crear_cliente'),
    path('editarCliente/<int:pk>', EditarCliente.as_view(), name='editar_cliente'),
    path('eliminarCliente/<int:pk>', EliminarCliente.as_view(), name='eliminar_cliente'),
    path('catalogo', CatalogoServicios.as_view(), name = 'catalogo'),
    path('about', About.as_view(), name = 'about'),
    path('apis/', include(router.urls)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)