from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView, TemplateView

from catalog.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"



