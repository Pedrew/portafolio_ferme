from django.shortcuts import render
from .models import Boletas
from django.shortcuts import redirect

# Create your views here.

def boletas_list(request):
	boletas = Boletas.getBoletas()
	return render(request, 'boletas/boleta_list.html',{ 'boletas' : boletas})

def boleta_detail(request):
	get = request.GET
	id_boleta = get['id']
	boleta = Boletas.getBoletaDetail(id_boleta)
	return render(request, 'boletas/boleta_detail.html',{ 'boleta' : boleta})
