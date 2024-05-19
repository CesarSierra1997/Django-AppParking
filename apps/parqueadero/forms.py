from django import forms
from .models import *

class ConjuntoForm(forms.ModelForm):
    class Meta:
        model = Conjunto
        fields = ['nombre','direccion']
        labels = {
            'nombre': 'Nombre del conjunto',
            'direccion': 'direccion del conjunto'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite el nombre del conjunto'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite la direccion del conjunto'}),
        }

class ParqueaderoForm(forms.ModelForm):
    class Meta:
        model = Parqueadero
        fields = ['numero','tipoVehiculo','tipo','activo','conjunto']
        labels = {
            'numero': 'Numero de parqueadero',
            'tipoVehiculo': 'Tipo de vehiculo',
            'tipo': 'Tipo de parqueadero',
            'activo': 'Parqueadero activo',
            'conjunto': 'Conjunto'
        }
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite numero de parqueadero'}),
            'tipoVehiculo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el tipo de vehiculo'}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el tipo de parqueadero'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Parqueadero activo'}),
            'conjunto': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el conjunto'}),
        }

class NovedadForm(forms.ModelForm):
    class Meta:
        model = Novedad
        fields = '__all__'

class ParqueaderoPropietarioForm(forms.ModelForm):
    class Meta:
        model = ParqueaderoPropietario
        fields = ['placa','apartamento','nombre','fecha_fin','parqueadero']
        labels = {
            'placa': 'Placa del vehiculo',
            'apartamento': 'Apartamento del residente',
            'nombre': 'Nombre de propieratio',
            'fecha_fin': 'Fecha de salida',
            'parqueadero': 'Parqueadero'
        }
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite la Placa del vehiculo'}),
            'apartamento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite apartamento de residencia'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite el nombre del porpietario'}),
            'fecha_fin': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'Digite la fecha de salida'}),
            'parqueadero': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione el parqueadero'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar los parqueaderos activos
        self.fields['parqueadero'].queryset = Parqueadero.objects.filter(activo=True)


class ParqueaderoVisitanteForm(forms.ModelForm):
    class Meta:
        model = ParqueaderoVisitante
        fields = '__all__'
