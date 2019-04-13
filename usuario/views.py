from django.shortcuts import render

# Create your views here.
def perfil(request):
	return render(request, 'usuario/perfil.html')


def login(request):
	return render(request, 'usuario/login.html')