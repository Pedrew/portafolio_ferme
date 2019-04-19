from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home/index.html')

def productos(request):
	return render(request, 'productos/product_list.html')