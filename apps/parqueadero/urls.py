from django.urls import path
from .views import (
    crear_parqueadero, editar_parqueadero, borrar_parqueadero, lista_parqueaderos,
    agregar_parqueaderoPropietario, editar_parqueaderoPropietario, eliminar_parqueaderoPropietario, listar_parqueaderoPropietario,
    agregar_parqueaderoVisitante, editar_parqueaderoVisitante, eliminar_parqueaderoVisitante, listar_parqueaderoVisitante,
)

urlpatterns = [
    # URLs para Parqueadero
    path('parqueadero/crear/', crear_parqueadero, name='crear_parqueadero'),
    path('parqueadero/<int:pk>/editar/', editar_parqueadero, name='editar_parqueadero'),
    path('parqueadero/<int:pk>/borrar/', borrar_parqueadero, name='borrar_parqueadero'),
    path('parqueaderos/', lista_parqueaderos, name='lista_parqueaderos'),

    # URLs para ParqueaderoPropietario
    path('parqueadero_propietario/agregar/', agregar_parqueaderoPropietario, name='agregar_parqueaderoPropietario'),
    path('parqueadero_propietario/<int:pk>/editar/', editar_parqueaderoPropietario, name='editar_parqueaderoPropietario'),
    path('parqueadero_propietario/<int:pk>/eliminar/', eliminar_parqueaderoPropietario, name='eliminar_parqueaderoPropietario'),
    path('parqueadero_propietario/listar/', listar_parqueaderoPropietario, name='listar_parqueaderoPropietario'),

    # URLs para ParqueaderoVisitante
    path('parqueadero_visitante/agregar/', agregar_parqueaderoVisitante, name='agregar_parqueaderoVisitante'),
    path('parqueadero_visitante/<int:pk>/editar/', editar_parqueaderoVisitante, name='editar_parqueaderoVisitante'),
    path('parqueadero_visitante/<int:pk>/eliminar/', eliminar_parqueaderoVisitante, name='eliminar_parqueaderoVisitante'),
    path('parqueadero_visitante/listar/', listar_parqueaderoVisitante, name='listar_parqueaderoVisitante'),
]
