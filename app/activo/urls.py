from abc import abstractproperty
from django.urls import path

from .views import *

urlpatterns = [
    path("", estadistica,name="estadistica"),
    path("index", ActivoList.as_view(),name="ListaActivos"),
    path("create", CreateActivo.as_view(),name="CrearActivo"),
    path("update/<int:pk>", UpdateActivo.as_view(),name="EditarActivo"),
]