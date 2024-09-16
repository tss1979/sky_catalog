from django.urls import path
from .views import index, contacts, product_detail

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    # path('product/<int:pk>', ProductDetail.as_view()),
    path('product/<int:pk>', product_detail, name='product_detail'),
]