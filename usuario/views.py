from django.shortcuts import render
from .models import Usuario
from django.shortcuts import redirect

# Create your views here.
def perfil(request):
	return render(request, 'usuario/perfil.html')

def login(request):
	return render(request, 'usuario/login.html')

def users_list(request):
	users_list = Usuario.getUsers()
	return render(request, 'usuario/user_list.html',{ 'user' : users_list})

def users_create(request):
	return render(request, 'usuario/user_create.html')

def users_insert(request):
	post = request.POST
	user = post['usuario']
	password = post['password']
	user_type = post['user_type']
	name = post['name']
	last_name = post['last_name']
	status = post['status']
	Usuario.createUser(user, password, user_type, name, last_name, status)
	response = redirect('users_list')
	return response

def users_delete(request):
	get = request.GET
	user_id = get['id']
	Usuario.deleteUser(user_id)
	response = redirect('users_list')
	return response

def users_get(request):
	get = request.GET
	user_id = get['id']
	response = Usuario.getUser(user_id)
	return render(request, 'usuario/user_update.html',{'user':response})

def users_update(request):
	post = request.POST
	user_id = post['id']
	user = post['usuario']
	password = post['password']
	user_type = post['user_type']
	name = post['name']
	last_name = post['last_name']
	status = post['status']
	Usuario.updateUser(user_id, user, password, user_type, name, last_name, status)
	response = redirect('users_list')
	return response