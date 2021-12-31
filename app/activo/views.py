from django.contrib.messages.api import success
from django.db import models
from django.db.models.query_utils import select_related_descend
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages

from .forms import ActivoForms
from .models import Activo
from ..direccionip.models import Direccionip
from ..agencia.models import Agencia
from ..gateway.models import Gateway
from ..categoria.models import Categoria

class ActivoList(ListView):
    model = Activo
    template_name = 'activo/index.html'
    paginate_by = 10

class CreateActivo(CreateView):
    model = Activo
    form_class = ActivoForms
    template_name = 'activo/create.html'
    success_url = reverse_lazy('CrearActivo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        direccionip = Direccionip.objects.all()
        agencia = Agencia.objects.all()
        gateway = Gateway.objects.all()
        categoria = Categoria.objects.all()
        context['direccionip'] = direccionip
        context['agencia'] = agencia
        context['gateway'] = gateway
        context['categoria'] = categoria
        return context

    def post(self, request, *args, **kwargs):
        try:
            activo = Activo()
            activo.nombre = request.POST['nombre']
            activo.descripcion = request.POST['descripcion']
            activo.id_agenciaFK = request.POST['id_agenciaFK']
            activo.id_categoriaFK = request.POST['id_categoriaFK']
            activo.id_direccionipFK = request.POST['id_direccionipFK']
            activo.id_gatewayFK = request.POST['id_gatewayFK']
            activo.save()
            messages.success(request,"El activo "+request.POST['nombre']+" fue registrado exitosamente!")
        except Exception as e:
            messages.error(request,"se produjo un error al registrar el activo, error: " + str(e))
        return redirect(self.success_url)

class UpdateActivo(UpdateView):
    model = Activo
    form_class = ActivoForms
    template_name = 'activo/update.html'
    success_url = reverse_lazy('ListaActivos')

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       direccionip = Direccionip.objects.all()
       agencia = Agencia.objects.all()
       gateway = Gateway.objects.all()
       categoria = Categoria.objects.all()
       context['direccionip'] = direccionip
       context['agencia'] = agencia
       context['gateway'] = gateway
       context['categoria'] = categoria
       return context

def estadistica(request):
    data = {}
    data['cantidad_usadas'] = Direccionip.objects.filter(estado = 1).count()
    data['cantidad_libres'] = Direccionip.objects.filter(estado = 0).count()

    data['gateway_cpa'] = Activo.objects.filter(id_gatewayFK__direccion = "192.168.0.10").count()
    data['gateway_sai'] = Activo.objects.filter(id_gatewayFK__direccion = "192.168.0.11").count()
    data['gateway_si'] = Activo.objects.filter(id_gatewayFK__direccion = "192.168.0.12").count()
    data['gateway_ln'] = Activo.objects.filter(id_gatewayFK__direccion = "192.168.0.13").count()
    data['gateway_sc'] = Activo.objects.filter(id_gatewayFK__direccion = "192.168.0.14").count()
    data['gateway_om'] = Activo.objects.filter(id_gatewayFK__direccion = "192.168.0.15").count()
    data['gateway_cbb'] = Activo.objects.filter(id_gatewayFK__direccion = "192.168.0.16").count()
    data['gateway_po'] = Activo.objects.filter(id_gatewayFK__direccion = "192.168.0.17").count()
    data['gateway_pa'] = Activo.objects.filter(id_gatewayFK__direccion = "192.168.0.18").count()
    return render(request,'activo/estadistica.html',data)