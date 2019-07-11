from django.shortcuts import render
from .models import Facturas
from django.shortcuts import redirect

# Create your views here.

def facturas_list(request):
	facturas = Facturas.getFacturas()
	return render(request, 'facturas/factura_list.html',{ 'facturas' : facturas})

def factura_detail(request):
	get = request.GET
	id_boleta = get['id']
	factura = Facturas.getFacturasDetail(id_boleta)
	return render(request, 'facturas/factura_detail.html',{ 'factura' : factura})
