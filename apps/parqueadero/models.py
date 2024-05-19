from django.db import models

class Conjunto(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Parqueadero(models.Model):
    numero = models.IntegerField()
    TIPO_VEHICULO = [
        ('Moto','Parqueadero para motos'),
        ('Carro','Parqueadero para carros'),
        ('Bicicleta','Parqueadero para bicicletas'),
    ]
    tipoVehiculo = models.CharField('tipo de vehiculo', max_length=100, choices=TIPO_VEHICULO)
    TIPO_PARQUEADERO = [
        ('Propietario','Parqueadero para propietarios'),
        ('Visitante','Parqueadero para visitantes')
    ]
    tipo = models.CharField('tipo de parqueadero', max_length=100, choices=TIPO_PARQUEADERO)
    activo = models.BooleanField(default=True)
    conjunto = models.ForeignKey(Conjunto, on_delete=models.CASCADE)
    def __str__(self):
        return f"Parqueadero {self.numero} - {self.tipo}"

class Novedad(models.Model):
    novedad = models.CharField(max_length=200)
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE)

    def __str__(self):
        return self.novedad

class ParqueaderoPropietario(models.Model):
    placa = models.CharField(max_length=20)
    apartamento = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(blank=False, null=False)
    parqueadero = models.OneToOneField(Parqueadero, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa

class ParqueaderoVisitante(models.Model):
    placa = models.CharField(max_length=20)
    apartamento = models.CharField(max_length=50)
    tipo_doc = models.CharField(max_length=20)
    documento = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    hora_ingreso = models.DateTimeField()
    hora_salida = models.DateTimeField(null=True, blank=True)
    parqueadero = models.OneToOneField(Parqueadero, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa
