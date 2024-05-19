from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Conjunto)

class ParqueaderoPropietarioInline(admin.TabularInline):
    model = ParqueaderoPropietario

class ParqueaderoVisitanteInline(admin.TabularInline):
    model = ParqueaderoVisitante

class ParqueaderoAdmin(admin.ModelAdmin):
    inlines = []

    def get_inline_instances(self, request, obj=None):
        if obj and obj.tipo == 'Propietario':
            self.inlines = [ParqueaderoPropietarioInline]
        elif obj and obj.tipo == 'Visitante':
            self.inlines = [ParqueaderoVisitanteInline]
        else:
            self.inlines = []
        return super().get_inline_instances(request, obj)

admin.site.register(Parqueadero, ParqueaderoAdmin)