from django import forms
from .models import Visita, Asesoria,Capacitacion,Cliente,SolicitudAsesoria, Profesional, Checklist, Condicion, DetChecklist, ContratoServicio, Accidente, Pago
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,User

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = ['fecha','asistentes','id_solicitud','descripcion_capa','id_estado']
        labels = {
            'fecha': 'Fecha de capacitacion',
            'asistentes': 'Cliente asociado',
            'id_solicitud': 'Profesional asociado',
            'descripcion_capa': 'Descripcion capacitacion',
            'id_estado': 'asistentes',
        }
        widgets = {
            'fecha'           : forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'descripcion_capa': forms.TextInput(attrs={'class': 'form-control'}),
            }
     
  

#class ProfesionalForm(forms.ModelForm):
#    class Meta:
#        model = Profesional
#        fields = '__all__'

class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese un nombre de usuario',
        'class': 'form-control',
        'autocomplete': 'off'

    }))

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['rut_profesional', 'nombre', 'paterno', 'materno']
        labels = {
          'rut_profesional': 'Rut profesional',
          'nombre ': 'Nombre',
          'paterno ': 'Apellido Paterno',
          'materno': 'Apellido Materno',
          }
        widgets = {
            'rut_profesional': forms.TextInput(attrs={'class': 'form-control', 'name':'rut_profesional',"onkeyup":"modifyText()" ,"id":"txtRut" , 'placeholder':'Formato: xxxxxxxx-x', "maxlength":"10"}),
            'nombre'          : forms.TextInput(attrs={'class': 'form-control', 'name':'nombre'}),
            'paterno'         : forms.TextInput(attrs={'class': 'form-control', 'name':'paterno'}),
            'materno'         : forms.TextInput(attrs={'class': 'form-control', 'name':'materno'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['id_cliente', 'nombre', 'rubro','direccion']
        labels = {

          'id_cliente': 'Rut Empresa',
          'nombre': 'Nombre Empresa',
          'direccion': 'Dirección',
          'rubro': 'Rubro',
          }
        widgets = {
            'id_cliente' : forms.TextInput(attrs={'class': 'form-control', 'id':'txtRut',"onkeyup":"modifyText()" , 'placeholder':'Formato: xxxxxxxx-x', "maxlength":"10"}),
            'direccion' : forms.TextInput(attrs={'class': 'form-control', 'id':'search_input'}),
            'nombre'     : forms.TextInput(attrs={'class': 'form-control'}),
            'rubro'      : forms.TextInput(attrs={'class': 'form-control', 'name':'rubro'}),
        }


class AsesoriasForm(forms.ModelForm):
    class Meta:
        model = Asesoria
        fields = [ 'fecha', 'id_solicitud']

    fecha                   = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['fecha', 'id_solicitud','descripcion', 'fecha', 'id_estado']
        labels = {
          'id_solicitud': 'id solicitud',
          'descripcion': 'Descripcion',
          'fecha': 'Fecha de la Visita',
          'id_estado': 'Id estado',
          }
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control','type':'date',"id":"datefield"}),
            'descripcion'   : forms.TextInput(attrs={'class': 'form-control'}),
        }




class SolicitudForm(forms.ModelForm):
    class Meta:
        model = SolicitudAsesoria
        fields = [ 'id_cliente', 'id_profesional', 'tipo_solicitud', 'descripcion_asesoria']

    #id_cliente             = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    tipo_solicitud           = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion_asesoria    = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


    
class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['descripcion_check','id_cliente']
        descripcion_check = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
        id_cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class DetChecklistForm(forms.ModelForm):
    class Meta:
        model = DetChecklist
        fields = ['checklist_nro_checklist','condicion_id_condicion']
        checklist_nro_checklist = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        condicion_id_condicion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class CondicionForm(forms.ModelForm):
    class Meta:
        model = Condicion
        fields = ['nom_condicion']
        labels = {
          'nom_condicion': 'Descripcion condicion',
          }
        widgets = {
            'nom_condicion': forms.Textarea(attrs={'class': 'form-control'}),

        }



class ContratoForm(forms.ModelForm):
    class Meta:
        model = ContratoServicio
        fields = ['fecha_inicio', 'fecha_termino', 'id_cliente', 'id_profesional']
        labels = {
          'fecha_inicio': 'Fecha de inicio',
          'fecha_termino': 'Fecha de termino',
          'id_cliente': 'ID del cliente',
          'id_profesional': 'ID Profesional',
          }
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
           
        }

class AccidenteForm(forms.ModelForm):
    class Meta:
        model = Accidente
        fields = ['id_cliente','descripcion']
        labels = {
          'id_cliente': 'cliente',
          'descripcion': 'Descripcion del accidente',
          }
        widgets = {
            'id_cliente'   : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion'   : forms.TextInput(attrs={'class': 'form-control'}),
        }

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['pago','fecha_pago']
        labels = {
          'pago': 'Total Pagado',
          'fecha_pago': 'Fecha del pago',
          }


class UserCreationFor(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1','password2','email')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email =     forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))