import re
import cx_Oracle
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profesional, Visita, Asesoria, Checklist, DetChecklist, Condicion, Cliente, Capacitacion,SolicitudAsesoria, Condicion, ContratoServicio # Llamado a los modelos
from .forms import VisitaForm, ResetPasswordForm, AsesoriasForm, ProfesionalForm, ChecklistForm, DetChecklistForm,CapacitacionForm , SolicitudForm, ClienteForm, CondicionForm, ContratoForm,UserCreationFor
from django.urls import reverse_lazy
from django.db import connection
from django.views.generic import View
from .utils import render_to_pdf, link_callback
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.models import User,Group
from django.core.mail import send_mail
from django.conf import settings
# profesional prueba como logeado rut= 172876595
# cliente prueba cmo logeado rut=2003901


######################################################################## URLS
def inicio(request):

    return render(request, "logins/ndex.html")

def servicios(request):

    return render(request, "logins/servicios.html")

def Contacto(request):

    return render(request, "logins/Contacto.html")

def Somos(request):

    return render(request, "logins/Somos.html")

######################################################################## CAPACITACION


def solicitudesC(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("tipocapacitacion", [x, out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def crearCapacitaciones(request,id):
    data = {
        'solicitudes' : solicitudesC(id),
    }

    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        asistentes = request.POST.get('asistentes')
        id_solicitud = request.POST.get('id_solicitud')
        descripcion_capa = request.POST.get('descripcion_capa')
        salida = agregarcapacitacion(fecha,asistentes,id_solicitud,descripcion_capa)
        if salida == 1:
            data['mensaje'] = 'agregado'
        else:
            data['mensaje'] = 'error'

    return render(request, "CapacitacionesCRUD/crearCapacitaciones.html", data)

def agregarcapacitacion(fecha,asistentes,id_solicitud,descripcion_capa):
    
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('agregar_capacitacion',[fecha,asistentes,id_solicitud,descripcion_capa, salida])
    
    return salida.getvalue()


def editarCapacitaciones(request, nro_capacitacion):
    capacitacion = Capacitacion.objects.get(nro_capacitacion = nro_capacitacion)
    formularioCapacitacion = {
        'form':CapacitacionForm(instance=capacitacion)
    }

    if request.method =='POST':
        formulario = CapacitacionForm(data=request.POST, instance=capacitacion)
        if formulario.is_valid():
            formulario.save()
            formularioCapacitacion['mensaje'] = "Modificado correctamente"
            formularioCapacitacion['form'] = formulario
    return render(request, "CapacitacionesCRUD/editarCapacitaciones.html", formularioCapacitacion)

def eliminarCapacitaciones(request, nro_capacitacion):
    capacitacion = Capacitacion.objects.get(nro_capacitacion = nro_capacitacion)
    capacitacion.delete()

    return redirect(to="listadoCapacitaciones")

######################################################################## PROFESIONALES
def listadoProfesionales(request):

    profesionales = Profesional.objects.all() #Error boligatorio, si compila 
    datosprof = {
        'profesionales':profesionales
    }

    return render(request, "ProfesionalesCRUD/listadoProfesionales_N.html", datosprof)

def crearProfesionales(request):
    if request.method == 'GET':
        form = ProfesionalForm()
        formularioProfesional = {   #Error obligatorio, si compila
            'form':form
    }
    else:
       form = ProfesionalForm(request.POST)
       
       if form.is_valid():
           form.save()
           return redirect('register_Profesional')
    return render(request, "ProfesionalesCRUD/crearProfesionales_N.html", {'form':form})


def editarProfesionales(request, rut_profesional):
    profesional = Profesional.objects.get(rut_profesional = rut_profesional) #Error obligatorio, si compila
    formularioProfesional = {   
        'form':ProfesionalForm(instance=profesional)
    }

    if request.method == 'POST':
        formulario = ProfesionalForm(data=request.POST, instance=profesional)
        if formulario.is_valid():
            formulario.save()
            formularioProfesional['mensaje'] = "Modificado Correctamente"
            formularioProfesional['form'] = formulario
            return redirect('listadoProfesionales')
    return render(request, 'ProfesionalesCRUD/editarProfesionales.html', formularioProfesional)

def eliminarProfesionales(request, rut_profesional):
    profesional = Profesional.objects.get(rut_profesional = rut_profesional)  #Error obligatorio, si compila
    profesional.delete()


    return redirect(to="listadoProfesionales")

######################################################################## VISITAS


def solicitudesV(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("tipovisita", [x, out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def crearVisitas(request,id):
    
    data = {
        'solicitudes': solicitudesV(id),
    }
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        id_solicitud = request.POST.get('id_solicitud')
        descripcion = request.POST.get('descripcion')
        nro_checklist = request.POST.get('nro_checklist')
        salida = crear_visita(fecha,id_solicitud,descripcion,nro_checklist)
        if salida == 1:
            data['mensaje'] = 'Visita Creada'
        else:
            data['mensaje'] = 'error'

    return render(request, "VisitasCRUD/crearVisitas.html", data)

def crear_visita(fecha,id_solicitud,descripcion,nro_checklist):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_VISITA',[ fecha,id_solicitud,descripcion,nro_checklist,salida])
    return salida.getvalue()

def editarVisitas(request, id_visita):
    visita = Visita.objects.get(id_visita = id_visita) #Error obligatorio, si compila
    formularioVisita = {   
        'form':VisitaForm(instance=visita)
    }

    if request.method == 'POST':
        formulario = VisitaForm(data=request.POST, instance=visita)
        if formulario.is_valid():
            formulario.save()
            formularioVisita['mensaje'] = "Modificado Correctamente"
            formularioVisita['form'] = formulario
    return render(request, 'VisitasCRUD/editarVisitas.html', formularioVisita)

def eliminarVisitas(request, id_visita):
    visita = Visita.objects.get(id_visita = id_visita)  #Error obligatorio, si compila
    visita.delete()


    return redirect(to="listadoVisitas")

######################################################################## CLIENTES

def rubros():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("RUBROS", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def agregarcliente(id_cliente,direccion, nombre,rubro):
    
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_CLIENTE',[id_cliente, direccion, nombre,rubro,salida])
    
    return salida.getvalue()

def listadoClientes(request):
    data = {
        'cliente':listado_Clientes()
    }
    return render(request, 'ClienteCRUD/listadoCliente.html',data)

def listado_Clientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("CLIENTES", [out_cur])
    lista = []
    for fila in out_cur: 
        lista.append(fila)
    return lista

def crearClientes(request):
    data = {
        'rubros' : rubros(),
    }
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        direccion = request.POST.get('direccion')
        rubro = request.POST.get('rubro')
        nombre = request.POST.get('nombre')
        salida = agregarcliente(id_cliente,direccion,nombre,rubro)
        if salida == 1:
            data['mensaje'] = 'agregado'
            return redirect('register_Cliente')
        else:
            data['mensaje'] = 'error'
    return render(request, 'ClienteCRUD/crearCliente.html',data)



def editarClientes(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente = id_cliente) #Error obligatorio, si compila
    formularioClientes = {   
        'form':ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            formularioClientes['mensaje'] = "Modificado Correctamente"
            formularioClientes['form'] = formulario
            return redirect('listadoCliente')
    return render(request, 'ClienteCRUD/editarCliente.html', formularioClientes)

def eliminarClientes(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente = id_cliente)  #Error obligatorio, si compila
    cliente.delete()

    return redirect(to="listadoCliente")

######################################################################## ASESORIAS

def listadoAsesorias(request,id):
    data = {
        'asesoria':listado_Asesorias(id)
    }
    return render(request, 'AsesoriasCRUD/listadoAsesorias.html',data)

def listado_Asesorias(id_pro):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 

    cursor.callproc("SP_LISTAR_ASESORIA", [id_pro,out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def solicitudesA(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("tipoasesoria", [x, out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def crearAsesorias(request,id):
    
    data = {
        'solicitudes': solicitudesA(id),
    }
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        id_solicitud = request.POST.get('id_solicitud')
        salida = crear_asesoria(fecha,id_solicitud)
        if salida == 1:
            data['mensaje'] = 'Asesoria Creada'
            return redirect('listadoAsesorias')
        else:
            data['mensaje'] = 'error'

    return render(request, "AsesoriasCRUD/crearAsesorias.html", data)

def crear_asesoria(fecha,id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_ASESORIA',[ fecha,id_solicitud,salida])
    return salida.getvalue()

def editarAsesorias(request, id_asesoria):
    asesoria = Asesoria.objects.get(id_asesoria = id_asesoria) #Error obligatorio, si compila
    formularioAsesorias = {   
        'form':AsesoriasForm(instance=asesoria)
    }

    if request.method == 'POST':
        formulario = AsesoriasForm(data=request.POST, instance=asesoria)
        if formulario.is_valid():
            formulario.save()
            formularioAsesorias['mensaje'] = "Modificado Correctamente"
            formularioAsesorias['form'] = formulario
            return redirect('listadoAsesorias')
    return render(request, 'AsesoriasCRUD/editarAsesorias.html', formularioAsesorias)

def eliminarAsesorias(request, id_asesoria):
    asesoria = Asesoria.objects.get(id_asesoria = id_asesoria)  #Error obligatorio, si compila
    asesoria.delete()

    return redirect(to="listadoAsesorias")

######################################################################## SOLICITUDES

def listado_tiposolicitud():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("tiposolicitud", [out_cur])
    lista = []
    for fila in out_cur: 
        lista.append(fila)
    return lista


def crearSolicitud(request,id):
    data = {
        'tiposolicitud': listado_tiposolicitud(),
        'info': infocontrato(id),
    }
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        id_profesional = request.POST.get('id_profesional')
        tipo_solicitud = request.POST.get('tipo_solicitud')
        descripcion_asesoria = request.POST.get('descripcion')
        salida = crear_solicitud(id_cliente, id_profesional,tipo_solicitud,descripcion_asesoria)
        if salida == 1:
            data['mensaje'] = 'agregado'
        else:
            data['mensaje'] = 'error'
    return render(request, "SolicitudCRUD/crearSolicitud.html", data)

def infocontrato(request,id)
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("contratoprocli", [x,out_cur])
    lista = []
    for fila in out_cur: 
        lista.append(fila)
    return lista

def crear_solicitud( id_cliente, id_profesional,tipo_solicitud,descripcion_asesoria):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_SOLICITUD',[ id_cliente, id_profesional,tipo_solicitud,descripcion_asesoria,salida])
    
    return salida.getvalue()


############################Funcion Crear Checklist 1era Parte

def listado_clienteProfesional(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("LISTADO_CLIENTEPROFESIONAL", [x,out_cur])
    lista = []
    for fila in out_cur: 
        lista.append(fila)
    return lista
################ID PROF3ESIONAL LOGEAOO PLSS (REQUEST, ID)
def crearChecklist(request,id):
    
    data = {
        'cliente' : listado_clienteProfesional(id),
    }
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion_check')
        id_cliente = request.POST.get('idcliente')
        salida = crear_checklist(descripcion, id_cliente)
        if salida == 1:
            data['mensaje'] = 'agregado'
            return redirect('siguienteChecklist')
        else:
            data['mensaje'] = 'Ya existe un Checklist asociado a este cliente.', id_cliente
            
    return render(request, 'ChecklistCRUD/crearChecklist.html',data)

def crear_checklist(descripcion, id_cliente):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('CREAR_CHECKLIST',[ descripcion, id_cliente,salida])
    
    return salida.getvalue()
######################################################### CHECKLIST 2DA PARTE
def siguienteCheck(request):
    if request.method == 'GET':
        form = DetChecklistForm()
        condicion = Condicion.objects.all().order_by('id_condicion').reverse
        checklist = Checklist.objects.all().order_by('nro_checklist').last

        formularioChecklist1 = {  
            'condicion' : condicion,
            'checklist' : checklist,
            'form':     form
    }
    
    else:
       form = DetChecklistForm(request.POST)
       if form.is_valid(): 
           form.save()
           return redirect('listadoAsesorias')
    return render(request, "ChecklistCRUD/crearChecklist2.html",formularioChecklist1)

def listadoChecklist(request):
    det_checklist = DetChecklist.objects.select_related('checklist_nro_checklist','condicion_id_condicion')
    checklist = Checklist.objects.all()
    datoscheck = {
        'checklist' : listado_checklist(),
         'joj' : checklist,
    }
    return render(request, "ChecklistCRUD/listadoChecklist.html", datoscheck)

def listado_checklist():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTAR_CHECK", [out_cur])
    lista = []
    for fila in out_cur: 
        lista.append(fila)
    return lista

def listadoDetSP(request): 
    hola = Checklist.objects.last()
    
    data = {
        'checklist' : listado_checklist(),
        'condicion' : listado_condicion(),
        'hola' :hola, 
    }
    data['listado'] = listado_detalle(hola.nro_checklist)
    if request.method == 'POST':
        checklist_nro_checklist = request.POST.get('idcheck')
        condicion_id_condicion = request.POST.get('idcond')
        salida = agregardetalle(checklist_nro_checklist, condicion_id_condicion)
        if salida == 1:
            data['mensaje'] = 'agregado'
            data['listado'] = listado_detalle(checklist_nro_checklist)
        else:
            data['mensaje'] = 'error'
            data['listado'] = listado_detalle(checklist_nro_checklist)

    return render(request, 'ChecklistCRUD/crearChecklist2.html',data)

def listado_condicion():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTAR_CONDICIONES", [out_cur])
    lista = []
    for fila in out_cur: 
        lista.append(fila)
    return lista

def listado_checklist():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTAR_CHECKLIST", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def agregardetalle(checklist_nro_checklist, condicion_id_condicion):
    
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_DETCHECK',[checklist_nro_checklist , condicion_id_condicion, salida])
    
    return salida.getvalue()

def eliminarDetalle(request, id ):
    eliminado = DetChecklist.objects.get(id_detchecklist = id )  #Error obligatorio, si compila
    eliminado.delete()

    return redirect(to="siguienteChecklist")


def eliminarChecklist(request, id ):
    salida = eliminardet(id)
    if salida == 1:
        eliminado = Checklist.objects.get(nro_checklist = id )  #Error obligatorio, si compila
        eliminado.delete()
            
    else:
        data['mensaje'] = 'error'
            

    return redirect(to="crearChecklist")

def eliminardet(iddetalle):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_DETALLE',[ iddetalle,salida])
    
    return salida.getvalue()

def completarChecklist(request, id):
    data = {
        'checklist' : listado_idchecklist(id),
        'listado' : listado_detalles(id), 
    }
    data['listado'] = listado_detalles(id)
    if request.method == 'POST':
        estado = request.POST.get('estado')
        act_mejora = request.POST.get('act_mejora')
        iddetalle = request.POST.get('iddetalle')
        salida = completardetalle(act_mejora, estado, iddetalle)
        if salida == 1:
            data['mensaje'] = 'agregado'
            data['listado'] = listado_detalles(id)
        else:
            data['mensaje'] = 'error'


    return render(request, 'ChecklistCRUD/completarChecklist.html',data)

def checklisto(request, id ):
    salida = check_listo(id)
    if salida == 1:
        return redirect('listadoChecklist')
            
    return redirect(to="listadoChecklist")

def check_listo(idcheck):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('checklisto',[ idcheck,salida])
    return salida.getvalue()

def completardetalle(act_mejora, estado , iddetalle):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_COMPLETAR_CHECK',[ act_mejora, estado, iddetalle,salida])
    
    return salida.getvalue()

def listado_detalles(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTAR_DETALLES", [ x,out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_idchecklist(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTA_CHECKLIST", [ x,out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listado_detalle(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTAR_DET", [ x,out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def verChecklist(request, id):
    data = {
        'checklist' : listado_idchecklist(id),
        'listado' : listado_detalles(id), 
    }
    return render(request, 'ChecklistCRUD/verChecklists.html',data)
    

#################################################################################################CONDICION

def listadoCondicion(request):

    condiciones = Condicion.objects.all() #Error boligatorio, si compila
    datos = {
        'condicion':condiciones
    }
    return render(request, "CondicionCRUD/listadoCondicion.html", datos)

def crearCondicion(request):
    accidente = ""
    data = {
        'mensaje': accidente,
    }
    if request.method == 'POST':
        nom_condicion = request.POST.get('nom_condicion')
        salida = crear_condicion(nom_condicion)
        if salida == 1:
            data['mensaje'] = 'agregado'
            return redirect('listadoCondicion')
        else:
            data['mensaje'] = 'error'
    return render(request, "CondicionCRUD/crearCondicion.html", data)

def crear_condicion(nom_condicion):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_CONDICION',[ nom_condicion,salida])
    return salida.getvalue()

def editarCondicion(request, id_condicion):
    condicion = Condicion.objects.get(id_condicion = id_condicion) #Error obligatorio, si compila
    formularioCon = {   
        'form':CondicionForm(instance=condicion)
    }

    if request.method == 'POST':
        formulario = CondicionForm(data=request.POST, instance=condicion)
        if formulario.is_valid():
            formulario.save()
            formularioCon['mensaje'] = "Modificado Correctamente"
            formularioCon['form'] = formulario
    return render(request, 'CondicionCRUD/editarCondicion.html', formularioCon)

def eliminarCondicion(request, id_condicion):
    condicion = Condicion.objects.get(id_condicion = id_condicion)  #Error obligatorio, si compila
    condicion.delete()


    return redirect(to="listadoCondicion")
######################################################################################################CONTRATOS
def listadoContrato(request):

    contrato = ContratoServicio.objects.all() #Error boligatorio, si compila
    datos = {
        'contrato':contrato
    }
    return render(request, "ContratoCRUD/listadoContrato.html", datos)

def crearContrato(request):
    
    data = {
        'clientes': listado_Clientes(),
        'profesional': listado_profesional(),
    }
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_termino = request.POST.get('fecha_termino')
        id_cliente =request.POST.get('id_cliente')
        id_profesional =request.POST.get('id_profesional')
        salida = crear_contrato(fecha_inicio, fecha_termino, id_cliente, id_profesional)
        if salida == 1:
            data['mensaje'] = 'agregado'
            return redirect('listadoContrato')
        else:
            data['mensaje'] = 'Este Cliente ya se encuentra asociado a un contrato'
    return render(request, "ContratoCRUD/crearContrato.html", data)

def crear_contrato(fecha_inicio,fecha_termino,id_cliente,id_profesional):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('AGREGAR_CONTRATO',[ fecha_inicio, fecha_termino, id_cliente, id_profesional,salida])           
    return salida.getvalue()     

def editarContrato(request, id_servicio):
    contrato = ContratoServicio.objects.get(id_servicio = id_servicio) #Error obligatorio, si compila
    formularioCon = {   
        'form':ContratoForm(instance=contrato)
    }

    if request.method == 'POST':
        formulario = ContratoForm(data=request.POST, instance=contrato)
        if formulario.is_valid():
            formulario.save()
            formularioCon['mensaje'] = "Modificado Correctamente"
            formularioCon['form'] = formulario
    return render(request, 'ContratoCRUD/editarContrato.html', formularioCon)

def listado_profesional():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("profesionales", [ out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

##########################################################################################ACCIDENTES
def reportarAccidente(id_cliente, descripcion):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_REPORT_ACCIDENT',[ id_cliente, descripcion,salida])
    return salida.getvalue()

def reporteAccidente(request):
    accidente = ""
    data = {
        'mensaje': accidente,
    }
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        descripcion = request.POST.get('descripcion')
        salida = reportarAccidente(id_cliente, descripcion)
        if salida == 1:
            data['mensaje'] = 'Reporte enviado'
        else:
            data['mensaje'] = 'Error Reporte NO enviado'
    return render(request, 'Accident/reportarAccidente.html',data)

def listadoAccidente(request,id):
    data = {
        'accidente':listado_accidentes(id)
    }
    return render(request, 'Accident/listadoAccidentes.html',data)

def listado_accidentes(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTAR_ACCIDENTE", [ x,out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listadoAccidentibilidad(request):

    data = {
        
        'accidente':listado_accidentibilidad()
    }
    return render(request, 'Accident/listadoAccidentibilidad.html',data)

def listado_accidentibilidad():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_accidentibilidad", [ out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

####################################################################VISTA PARA LA PAGINA LISTAR PAGOS
def listadoClientePago(request):

    cliente = Cliente.objects.all() #Error obligatorio, si compila
    datosclien = {
        'cliente':cliente
    }
    return render(request, "Accident/listadoClientePago.html", datosclien)


def listadoPagos(request, id_cliente):
    pago = listado_pagos(id_cliente)
    data = {
        'pago': pago
    }
    return render(request, 'Accident/listadoClientePagos.html',data)

####################################################################PROCEDIMIENTO PARA LISTAR LOS PAGOS
def listado_pagos(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTARPAGOS", [ x,out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

####################################################################ACTUALIZAR PAGO
def actualizarPago(request, id):

    data = {
        'pago' : listado_pago(id),
    }
    data['pago'] = listado_pago(id)
    if request.method == 'POST':
        pago = request.POST.get('pago')
        fecha_pago = request.POST.get('fecha_pago')
        idpago = request.POST.get('idpago')
        salida = actualizarunpago(pago, fecha_pago, idpago)
        if salida == 1:
            data['mensaje'] = 'agregado'
            data['listado'] = listado_pago(id)
        else:
            data['mensaje'] = 'error'

    return render(request, 'Accident/actualizaPago.html',data)

####################################################################LISTAR EL PAGO PARA TRAER ID DEL PAGO 
def listado_pago(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTARPAGO", [x,out_cur])
    lista = []
    for fila in out_cur: 
        lista.append(fila)
    return lista
####################################################################PROCEDIMIENTO PARA ACTUALIZAR UN PAGO
def actualizarunpago(pago, fecha , idpago):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ACTUALIZARPAGO',[ pago, fecha, idpago,salida])
    
    return salida.getvalue()

####################################################################listado actividades admin
def listadoActividadAdm(request):

    activity = actividadesAdmin()
    datosclien = {
        'activity':activity
    }
    return render(request, "Actividad/listadoActividadAdmin.html", datosclien)

def actividadesAdmin():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SPACTIVIDADESADMIN", [ out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

####################################################################listado actividades Cliente
def listadoActividadCliente(request):
    #reemplazar con el idcliente logiao
    activity = actividadesCliente(2003901)
    datosclien = {
        'activity':activity
    }
    return render(request, "Actividad/listadoActividadCliente.html", datosclien)

def actividadesCliente(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_ACT_CLIENTE", [x, out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

####################################################################listado actividades Profesional
def listadoActividadPro(request):
    #reemplazar con el idprofesional logiao
    activity = actividadesPro(172876595)
    datosclien = {
        'activity':activity
    }
    return render(request, "Actividad/listadoActividadProfesional.html", datosclien)

def actividadesPro(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_ACT_PROFESIONAL", [ x,out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

####################################################################listado atrasos
def listadoAtrasos(request):
    atraso = atrasos()
    datos = {
        'atraso':atraso
    }
    return render(request, "Actividad/listadoAtrasos.html", datos)

def atrasos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_ATRASOS", [ out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

###################################################################CLIENTES DEL PROFESIONAL
def listadoMisClientes(request,id):
    #reemplazar pa cuando se logee el profesional
    cliente = misclientes(id)
    datos = {
        'cliente':cliente
    }
    return render(request, "Actividad/listadoMisClientes.html", datos)

def misclientes(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_MISCLIENTES", [ x,out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

###################################################################PDF CHECKLIST

def render_pdf_view(request, id):
    template_path = 'ChecklistCRUD/verChecklistPDF.html'
    context = {           'checklist' : listado_idchecklist(id),
           'listado' : listado_detalles(id), }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

###################################################################ID CLIENTE LOGEADO
def verChecklistCliente(request):
    data = {
        'checklist' : listado_checklistcliente(2003901),
     
    }
    return render(request, 'ChecklistCRUD/listadoChecklistCliente.html',data)

def listado_detallescliente(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("LISTADO_DETALLESCLIENTE", [ x,out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_checklistcliente(x):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("LISTADO_CHECKLISTCLIENTE", [ x,out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def verChecklistCl(request, id):
    data = {
        'checklist' : listado_idchecklist(id),
        'listado' : listado_detalles(id), 
    }
    return render(request, 'ChecklistCRUD/verChecklistsCliente.html',data)


def register(request):
    if request.method == 'POST':
        form = UserCreationFor(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Cliente')
            user.groups.add(group)
            return redirect('servicios')
    else:
        form = UserCreationFor()
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, 'registration/register_Cliente.html', {'form': form})

def register2(request):
    if request.method == 'POST':
        form = UserCreationFor(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Profesional')
            user.groups.add(group)
            return redirect('servicios')
    else:
        form = UserCreationFor()
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, 'registration/register_Profesional.html', {'form': form})

def register3(request):
    if request.method == 'POST':
        form = UserCreationFor(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Administrador')
            user.groups.add(group)
            return redirect('servicios')
    else:
        form = UserCreationFor()
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, 'registration/register_Administrador.html', {'form': form})

####################################################################

def enviarCorreo(request,correo):
    subject='Información No + Accidentes'
    message='Comunicamos a usted que a la fecha mantiene una cuenta impaga de No+accidentes. Recuerde pagar sus cuentas a tiempo y evitará estos molestos contactos de cobranza.'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[correo]
    send_mail(subject,message,email_from,recipient_list,)
    return redirect(to="listadoAtrasos")

    ##############################################################

def listadoCapacitaciones(request,id):
    datoscapa = {
        'capacitacion':listado_capacitacion(id)
    }
    return render(request, "CapacitacionesCRUD/listadoCapacitaciones.html", datoscapa)

def listado_capacitacion(id_pro):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTAR_capacitacion", [id_pro,out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listadoVisitas(request,id):
    visitas=listado_visita(id)
    datosvisi = {
        'visitas':visitas
    }
    return render(request, "VisitasCRUD/listadoVisitas.html", datosvisi)

def listado_visita(id_pro):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() 
    cursor.callproc("SP_LISTAR_visita", [id_pro,out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

