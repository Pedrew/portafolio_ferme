from django.shortcuts import render
from .models import Reportes
from django.shortcuts import redirect

# Create your views here.
def boletas_anno(request, ano):
    post = request.POST
    anno = post['anno']
    boletas_ano = Reportes.boletasAnno(anno)
    return render(request, 'reportes/boletas_anno.html',{ 'boletas' : boletas_ano})
