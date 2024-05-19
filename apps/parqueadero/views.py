from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def inicio(request):
    return render(request, 'base.html')

# Vistas para Parqueadero
def crear_parqueadero(request):
    if request.method == 'POST':
        form = ParqueaderoForm(request.POST)
        if form.is_valid():
            parqueadero = form.save(commit=False)  # Crea una instancia de Parqueadero pero no la guarda en la BD
            parqueadero.activo = True  # Establece el campo activo como True
            parqueadero.save()  # Ahora guarda la instancia en la BD
            return redirect('lista_parqueaderos')
    else:
        form = ParqueaderoForm()
    return render(request, 'parqueadero/crear_parqueadero.html', {'form': form})

def editar_parqueadero(request, pk):
    parqueadero = get_object_or_404(Parqueadero, pk=pk)
    if request.method == 'POST':
        form = ParqueaderoForm(request.POST, instance=parqueadero)
        if form.is_valid():
            form.save()
            return redirect('lista_parqueaderos')
    else:
        form = ParqueaderoForm(instance=parqueadero)
    return render(request, 'parqueadero/editar_parqueadero.html', {'form': form})

def borrar_parqueadero(request, pk):
    parqueadero = get_object_or_404(Parqueadero, pk=pk)
    if request.method == 'POST':
        parqueadero.delete()
        return redirect('lista_parqueaderos')
    return render(request, 'parqueadero/confirmar_borrar_parqueadero.html', {'parqueadero': parqueadero})

def lista_parqueaderos(request):
    parqPropietarios = Parqueadero.objects.filter(tipo='Propietario')
    parqVisitantes = Parqueadero.objects.filter(tipo='Visitante')
    parqueaderos = Parqueadero.objects.all()
    parqueadero_propietarios = ParqueaderoPropietario.objects.all()
    parqueadero_visitantes = ParqueaderoVisitante.objects.all()
    return render(request, 'parqueadero/lista_parqueaderos.html', {
        'parqPropietarios': parqPropietarios,
        'parqVisitantes':parqVisitantes,
        'parqueaderos': parqueaderos,
        'parqueadero_propietarios':parqueadero_propietarios,
        'parqueadero_visitantes':parqueadero_visitantes
        })

# Vistas para ParqueaderoPropietario
def agregar_parqueaderoPropietario(request):
    if request.method == 'POST':
        form = ParqueaderoPropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_parqueaderoPropietario')
    else:
        form = ParqueaderoPropietarioForm()
    return render(request, 'propietario/agregar_parqueaderoPropietario.html', {'form': form})

def editar_parqueaderoPropietario(request, pk):
    parqueadero_propietario = get_object_or_404(ParqueaderoPropietario, pk=pk)
    if request.method == 'POST':
        form = ParqueaderoPropietarioForm(request.POST, instance=parqueadero_propietario)
        if form.is_valid():
            form.save()
            return redirect('listar_parqueaderoPropietario')
    else:
        form = ParqueaderoPropietarioForm(instance=parqueadero_propietario)
    return render(request, 'propietario/editar_parqueaderoPropietario.html', {'form': form})

def eliminar_parqueaderoPropietario(request, pk):
    parqueadero_propietario = get_object_or_404(ParqueaderoPropietario, pk=pk)
    if request.method == 'POST':
        parqueadero_propietario.delete()
        return redirect('listar_parqueaderoPropietario')
    return render(request, 'propietario/confirmar_eliminar_parqueaderoPropietario.html', {'parqueadero_propietario': parqueadero_propietario})

def listar_parqueaderoPropietario(request):
    parqueadero_propietarios = ParqueaderoPropietario.objects.all()
    return render(request, 'propietario/listar_parqueaderoPropietario.html', {'parqueadero_propietarios': parqueadero_propietarios})

# Vistas para ParqueaderoVisitante
def agregar_parqueaderoVisitante(request):
    if request.method == 'POST':
        form = ParqueaderoVisitanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_parqueaderoVisitante')
    else:
        form = ParqueaderoVisitanteForm()
    return render(request, 'visitante/agregar_parqueaderoVisitante.html', {'form': form})

def editar_parqueaderoVisitante(request, pk):
    parqueadero_visitante = get_object_or_404(ParqueaderoVisitante, pk=pk)
    if request.method == 'POST':
        form = ParqueaderoVisitanteForm(request.POST, instance=parqueadero_visitante)
        if form.is_valid():
            form.save()
            return redirect('listar_parqueaderoVisitante')
    else:
        form = ParqueaderoVisitanteForm(instance=parqueadero_visitante)
    return render(request, 'visitante/editar_parqueaderoVisitante.html', {'form': form})

def eliminar_parqueaderoVisitante(request, pk):
    parqueadero_visitante = get_object_or_404(ParqueaderoVisitante, pk=pk)
    if request.method == 'POST':
        parqueadero_visitante.delete()
        return redirect('listar_parqueaderoVisitante')
    return render(request, 'visitante/confirmar_eliminar_parqueaderoVisitante.html', {'parqueadero_visitante': parqueadero_visitante})

def listar_parqueaderoVisitante(request):
    parqueadero_visitantes = ParqueaderoVisitante.objects.all()
    return render(request, 'visitante/listar_parqueaderoVisitante.html', {'parqueadero_visitantes': parqueadero_visitantes})
