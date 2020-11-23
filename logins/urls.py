from django.contrib import admin
from django.urls import path, include
from logins import views
from django.conf import settings
from django.conf.urls.static import static
from .views import editarVisitas, eliminarVisitas, listadoVisitas #metodo para acotar ruta (no .html)
from .views import crearAsesorias, listadoAsesorias, editarAsesorias, eliminarAsesorias #metodo para acotar ruta (no .html)
from .views import crearProfesionales, listadoProfesionales, editarProfesionales, eliminarProfesionales #metodo para acotar ruta (no .html)
from .views import crearClientes, listadoClientes, editarClientes, eliminarClientes
from .views import  listadoChecklist, eliminarDetalle, eliminarChecklist, completarChecklist, completardetalle, verChecklist, checklisto
from .views import  crearSolicitud
from . import views
from .views import crearCondicion, listadoCondicion, editarCondicion, eliminarCondicion
from .views import crearContrato,listadoContrato, editarContrato, reporteAccidente, listadoAccidente, listadoPagos, actualizarPago, listadoActividadAdm, listadoAtrasos
from .views import enviarCorreo
# Definicion de las Urls
urlpatterns = [
    path('', views.inicio, name="ndex"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register_Cliente', views.register, name='register_Cliente' ),
    path('register_Profesional', views.register2, name='register_Profesional'),
    path('register_Administrador', views.register3, name='register_Administrador'),
 
    path("servicios", views.servicios, name="servicios"),
    path("Contacto.html", views.Contacto, name="Contacto"),
    path("Somos.html", views.Somos, name="Somos"),
       
    path("listadoCapacitaciones.html", views.listadoCapacitaciones, name="listadoCapacitaciones"),
    path("crearCapacitaciones.html", views.crearCapacitaciones, name="crearCapacitaciones"),
    path("editarCapacitaciones/<nro_capacitacion>", views.editarCapacitaciones, name="editarCapacitaciones"),
    path("eliminarCapacitaciones/<nro_capacitacion>", views.eliminarCapacitaciones, name="eliminarCapacitaciones"),

    path("listadoVisitas.html", views.listadoVisitas, name="listadoVisitas"), 
    path("crearVisitas.html", views.crearVisitas, name="crearVisitas"), 
    path('editarVisitas/<id_visita>', editarVisitas, name='editarVisitas'), 
    path('eliminarVisitas/<id_visita>', eliminarVisitas, name = 'eliminarVisitas'),

    path("listadoProfesionales_N.html", views.listadoProfesionales, name="listadoProfesionales"),
    path("crearProfesionales_N.html", views.crearProfesionales, name="crearProfesionales"),
    path('editarProfesionales/<rut_profesional>', editarProfesionales, name='editarProfesionales'), 
    path('eliminarProfesionales/<rut_profesional>', eliminarProfesionales, name = 'eliminarProfesionales'),

    path("listadoAsesorias.html", views.listadoAsesorias, name="listadoAsesorias"),
    path("crearAsesorias.html", views.crearAsesorias, name="crearAsesorias"),
    path('editarAsesorias/<id_asesoria>', editarAsesorias, name='editarAsesorias'), 
    path('eliminarAsesorias/<id_asesoria>', eliminarAsesorias, name = 'eliminarAsesorias'),
    
    path("listadoCliente.html", views.listadoClientes, name="listadoCliente"),
    path("crearCliente.html", views.crearClientes, name="crearCliente"),
    path('editarCliente/<id_cliente>', editarClientes, name='editarCliente'), 
    path('eliminarCliente/<id_cliente>', eliminarClientes, name = 'eliminarCliente'),

    path('crearSolicitud.html', crearSolicitud, name = 'crearSolicitud'),

    path("listadoChecklist.html", views.listadoChecklist, name="listadoChecklist"),
    path("crearChecklist.html", views.crearChecklist, name="crearChecklist"),
    path("crearChecklist2.html", views.listadoDetSP, name="siguienteChecklist"),
    path('eliminarDetalle/<id>', eliminarDetalle, name = 'eliminarDetalle'),
    path('eliminarChecklist/<id>', eliminarChecklist, name = 'eliminarChecklist'),
    path('completardetalle/<id>', completardetalle, name = 'completardetalle'),
    path('completarChecklist/<id>', completarChecklist, name = 'completarChecklist'),
    path("verChecklists/<id>", verChecklist, name="verChecklist"),
    path('checklisto/<id>', checklisto, name = 'checklisto'),

    path('listadoCondicion.html', views.listadoCondicion, name="listadoCondicion"),
    path("crearCondicion.html", views.crearCondicion, name="crearCondicion"),
    path('editarCondicion/<id_condicion>', editarCondicion, name='editarCondicion'), 
    path('eliminarCondicion/<id_condicion>', eliminarCondicion, name = 'eliminarCondicion'),

    path("crearContrato.html", views.crearContrato, name="crearContrato"),
    path('listadoContrato.html', views.listadoContrato, name="listadoContrato"),
    path('editarContrato/<id_servicio>', editarContrato, name='editarContrato'), 

    path("reportarAccidente.html", views.reporteAccidente, name="reporteAccidente"),
    path('listadoAccidentes.html', views.listadoAccidente, name="listadoAccidente"),
    path('listadoAccidentibilidad.html', views.listadoAccidentibilidad, name="listadoAccidentibilidad"),
    path('listadoClientePago.html', views.listadoClientePago, name="listadoClientePago"),
    path("verPagos/<id_cliente>", listadoPagos, name="verPagos"),
    path('actualizarPago/<id>', actualizarPago, name = 'actualizarPago'),
    
    path('listadoActividadAdmin.html', views.listadoActividadAdm, name="listadoActAdmin"),
    path('listadoActividadCliente.html', views.listadoActividadCliente, name="listadoActCliente"),
    path('listadoActividadProfesional.html', views.listadoActividadAdm, name="listadoActProfesional"),
    path('listadoAtrasos.html', views.listadoAtrasos, name="listadoAtrasos"),
    path('listadoMisClientes.html', views.listadoMisClientes, name="listadoMisClientes"),

    path("verChecklistPDF.html/<id>", views.render_pdf_view, name="verChecklistPDF"),

    path("listadoChecklistCliente.html", views.verChecklistCliente, name="listadoChecklistCliente"),
    path("verChecklistsCliente/<id>", views.verChecklistCl, name="verChecklistCliente"),

    path('enviarCorreo/<correo>', enviarCorreo, name = 'enviarCorreo'),
]
