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
	email = Usuario.validateUserEmail(user)
	if email == None:
		error = 'El email ingresado ya existe'
		return render(request, 'usuario/user_create.html',{'error': error })
	else:
		password = post['password']
		user_type = post['user_type']
		name = post['name']
		last_name = post['last_name']
		status = post['status']
		rut = post['rut']

		direccion = ""
		rubro = ""
		telefono = ""
		razon_social = ""
		identificador = ""
		if user_type == "4":
			rubro = post['rubro']
			telefono = post['telefono']
			razon_social = post['razon_social']
			identificador = post['identificador']
		if user_type == "3" or user_type == "6":
			direccion = post['direccion']
		Usuario.createUser(user, password, user_type, name, last_name, status, rut, rubro, telefono, razon_social, identificador, direccion)
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
	user_type = get['type']
	response = Usuario.getUser(user_id, user_type)
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
	rut = post['rut']
	Usuario.updateUser(user_id, user, password, user_type, name, last_name, status, rut)
	response = redirect('users_list')
	return response

def update_user_status(request):
	get = request.GET
	user_id = get['id']
	user_status = get['status']
	if user_status == 'Activo':
		user_status = 'Inactivo'
	else:
		user_status = 'Activo'
	response = Usuario.updateUserStatus(user_id, user_status)
	response = redirect('users_list')
	return response

def validate_user(request):
	post = request.POST
	user = post['usuario']
	password = post['password']
	response = Usuario.validateUser(user, password)
	if response == None:
		error = 'Los datos ingresados no son válidos'
		return render(request, 'home/login.html',{'error': error })
	else:
		return render(request, 'home/login.html',{'valid':response})
