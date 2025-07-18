from django.forms import ModelForm
from . models import Barang
from django import forms


class FormBarang(ModelForm):
    class Meta:
        model= Barang
        fields= '__all__'
        widgets = {
            'kdbrg': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'link_gbr': forms.URLInput(attrs={'class': 'form-control'}),
            'id_jenis': forms.Select(attrs={'class': 'form-control'}),
        }