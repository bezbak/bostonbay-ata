from django.shortcuts import render
from apps.settings.models import ADS    
from .models import Category, Product
# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all().filter(category_id=1)[:8]
    category = Category.objects.get(id=1)
    ads = ADS.objects.all().latest('id')
    context = {
        'categories':categories,
        'products':products,
        'ads':ads,
        'category':category,
    }
    return render(request, 'index.html',context)