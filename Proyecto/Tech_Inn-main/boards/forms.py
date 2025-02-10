from django import forms
from boards.models import *
from django.contrib.auth.forms import AuthenticationForm


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['documento', 'Nombre', 'Apellido', 'email', 'telefono', 'genero', 'estado', 'password', 'tipo', 'foto']
        widgets = {
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class HabitacionForm(forms.ModelForm):
    class Meta:
        model=Habitacion
        fields = ['numero', 'estado', 'caracteristicas', 'costo_base', 'capacidad', 'nro_cama_sencilla', 'nro_cama_doble', 'nro_camarotes', 'tipo', 'imagen']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'caracteristicas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'costo_base': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_cama_sencilla': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_cama_doble': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_camarotes': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),}

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'costo', 'stock_disponible', 'descripcion', 'id_tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_disponible': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_tipo': forms.Select(attrs={'class': 'form-control'}),
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'costo', 'id_tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_tipo': forms.Select(attrs={'class': 'form-control'}),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['documento', 'estado', 'cantidad_adultos', 'cantidad_niños', 'fecha_ingreso', 'fecha_salida', 'nro_habitacion', 'comentarios']
        widgets = {
            'documento': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}, choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada')]),
            'cantidad_adultos': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_niños': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'form-control'}),
            'nro_habitacion': forms.Select(attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['documento'].queryset = Usuarios.objects.all()
        self.fields['nro_habitacion'].queryset = Habitacion.objects.all()

class ConsumosForm(forms.ModelForm):
    class Meta:
        model = Consumos
        fields = ['id_Reserva', 'id_Servicio', 'cantidad_s', 'id_Producto', 'cantidad_p', 'total', 'facturado']
        widgets = {
            'id_Reserva': forms.Select(attrs={'class': 'form-control'}),
            'id_Servicio': forms.Select(attrs={'class': 'form-control'}),
            'cantidad_s': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_Producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad_p': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'facturado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ConsumosForm, self).__init__(*args, **kwargs)

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = ['id', 'tipo']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),}

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['categoria']
        widgets = {
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = ['rol']

        widgets = {
            'rol': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class TipoServicioForm(forms.ModelForm):
    class Meta:
        model = TipoServicio
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomAuthenticationForm(forms.Form):
    Nombre = forms.CharField(label='Usuario')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
