from django.shortcuts import render
from django.views.generic import DetailView, CreateView

from catalog.admin import ProductAdmin
from catalog.models import Product


# Create your views here.


def index(request):
    context = {'object_list': Product.objects.all()}
    return render(request, "catalog/home.html", context)

def contacts(request):
    if request.method == 'POST':
        print({
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'message': request.POST.get('message'),
        })
    return render(request, "catalog/contacts.html")

# class ProductDetail(DetailView):
#     model = Product
#     template_name = 'catalog/product.html'
#     context_object_name = 'product'


def product_detail(request, pk):
    template_name = 'catalog/product.html'
    context = {'product': Product.objects.get(pk=pk)}
    return render(request, template_name, context)

