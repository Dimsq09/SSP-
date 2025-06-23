from django.urls import path
from . import views

urlpatterns = [
    path('omah/', views.home ),
    path('produk/', views.produk),
]