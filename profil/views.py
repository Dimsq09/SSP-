from django.shortcuts import render
from .models import About
from .form import FormBarang


# Create your views here.
def home(request):
   about = About.objects.first()
   return render(request,'index.html',{'about':about})

def Team(request):
    return render(request,'our team.html')

def produk(request):
    return render(request,'produk.html')

def registrasi(request):
    return render(request,'registrasi.html')

def form_barang(request):
    from_barang = FormBarang()
    return render(request, 'Tambah.html', {'form_barang': from_barang})