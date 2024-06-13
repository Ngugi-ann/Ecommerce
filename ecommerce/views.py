from django.shortcuts import render
from . models import Products

# Create your views here.
def product_list(request):
    products = Products.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'Ecommerce/product_list.html', context)

    
