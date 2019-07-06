from django.shortcuts import render
from .models import Reportes
from django.shortcuts import redirect

# Create your views here.
def reportes(request):
    return render(request, 'reportes/reportes.html')

def boletas_anno(request):
    post = request.POST
    anno = post['ano']
    boletas_ano = Reportes.boletasAnno(anno)
    total = Reportes.boletasAnnoTotal(anno)
    return render(request, 'reportes/boletas_anno.html',{
    	'boletas' : boletas_ano,
    	'total' : total
    })

def boletas_mes(request):
    post = request.POST
    mes = post['mes']
    ano = post['ano']
    boletas_mes = Reportes.boletasMes(mes, ano)
    total = Reportes.boletasMesTotal(mes, ano)
    return render(request, 'reportes/boletas_mes.html',{
    	'boletas' : boletas_mes,
    	'total' : total
    })

def boletas_dia(request):
    post = request.POST
    mes = post['mes']
    ano = post['ano']
    dia = post['dia']
    boletas_dia = Reportes.boletasDia(dia, mes, ano)
    total = Reportes.boletasDiaTotal(dia, mes, ano)
    return render(request, 'reportes/boletas_dia.html',{
    	'boletas' : boletas_dia,
    	'total' : total
    })

def compras_usuario(request):
    compra_usuario = Reportes.comprasUsuario()
    return render(request, 'reportes/compra_usuario.html',{ 'compras' : compra_usuario})

def compras_metodo(request):
    post = request.POST
    tipoPago = post['tipo_pago']
    compras_metodo = Reportes.comprasMetodo(tipoPago)
    total = Reportes.comprasMetodoTotal(tipoPago)
    return render(request, 'reportes/compras_metodo.html',{
    	'boletas' : compras_metodo,
    	'total' : total
    })

def compras_lugar(request):
    post = request.POST
    lugarPago = post['lugar_pago']
    compras_lugar = Reportes.comprasEntrega(lugarPago)
    total = Reportes.comprasEntregaTotal(lugarPago)
    return render(request, 'reportes/compras_lugar.html',{
    	'boletas' : compras_lugar,
    	'total' : total
    })