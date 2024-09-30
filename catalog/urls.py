from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsTemplateView, ProductUpdateView, ProductCreateView, \
    ProductDeleteView, VersionUpdateView, VersionCreateView, VersionDeleteView, VersionListView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('create', ProductCreateView.as_view(), name='product_create'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('version/update/<int:pk>', VersionUpdateView.as_view(), name='version_update'),
    path('version/create', VersionCreateView.as_view(), name='version_create'),
    path('version/delete/<int:pk>', VersionDeleteView.as_view(), name='version_delete'),
    path('versions/', VersionListView.as_view(), name='versions'),
]