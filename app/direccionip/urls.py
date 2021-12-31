from django.urls import path
from .views import DireccionLibre

urlpatterns = [
    path('libre',DireccionLibre.as_view(),name="direccionLibre")
]