from django.shortcuts import render
from django.views.generic import ListView

from .models import Direccionip

class DireccionLibre(ListView):
    model = Direccionip
    template_name = 'direccionip/index.html'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(estado = 0)
