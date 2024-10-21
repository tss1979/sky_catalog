
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, TemplateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version
from catalog.services import get_cached_categories


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

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_published=True)
        return qs

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        product_form = form.save(commit=False)
        product_form.user = self.request.user
        return super().form_valid(product_form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('catalog:products')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return ProductForm
        elif user.has_perm("catalog.update_published_status") and user.has_perm("catalog.update_description") and \
             user.has_perm("catalog.change_category") :
            return ProductModeratorForm
        else:
            raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, DeleteView):
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


class CategoriesListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = get_cached_categories()
        return context

    template_name = "catalog.categories.html"



