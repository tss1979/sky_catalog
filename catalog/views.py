from itertools import product

from PIL.ImageCms import versions
from django.db.backends.mysql.base import version
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, TemplateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


# Create your views here.
class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        dict_product = {}
        for prod in context_data['object_list']:
            dict_product.setdefault(prod)
            dict_product[prod] = Version.objects.filter(is_current=True, product=prod).first()
        context_data['object_list'] = dict_product
        return context_data

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')

class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products')

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products')

class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:products')

class VersionListView(ListView):
    model = Version



