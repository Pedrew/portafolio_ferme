from django.shortcuts import render
from .models import Reportes
from django.shortcuts import redirect

# Create your views here.
def reportes(request):
    return render(request, 'reportes/reportes.html')

def boletas_anno(request):
    post = request.POST
    anno = post['anno']
    boletas_ano = Reportes.boletasAnno(anno)
    return render(request, 'reportes/boletas_anno.html',{ 'boletas' : boletas_ano})

def boletas_mes(request):
    post = request.POST
    mes = post['mes']
    ano = post['ano']
    boletas_mes = Reportes.boletasMes(mes, ano)
    return render(request, 'reportes/boletas_mes.html',{ 'boletas' : boletas_mes})

def boletas_dia(request):
    post = request.POST
    mes = post['mes']
    ano = post['ano']
    dia = post['dia']
    boletas_dia = Reportes.boletasDia(dia, mes, ano)
    return render(request, 'reportes/boletas_dia.html',{ 'boletas' : boletas_dia})