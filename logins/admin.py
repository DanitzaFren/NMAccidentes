from django.contrib import admin
from .models import Administrador, Asesoria, Capacitacion, Checklist, Cliente, Condicion, ContratoServicio, DetChecklist, Pago, Profesional, SolicitudAsesoria, Visita, AuthUser

admin.site.register(Administrador) 
admin.site.register(Asesoria) 
admin.site.register(Capacitacion) 
admin.site.register(Checklist) 
admin.site.register(Cliente)
admin.site.register(Condicion)
admin.site.register(ContratoServicio)
admin.site.register(DetChecklist)
admin.site.register(Pago)
admin.site.register(Profesional)
admin.site.register(SolicitudAsesoria)       
admin.site.register(Visita) 
admin.site.register(AuthUser) 
