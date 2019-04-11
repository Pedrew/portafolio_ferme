from django.shortcuts import render

# Create your views here.

def product_list(request):
    return render(request, 'product/templates/product/product_list.html', {})