from django.contrib import admin
from . models import Barang, Jenis, About
# Register your models here.

class BarangAdmin(admin.ModelAdmin):
    list_display = ('kdbrg', 'nama', 'stok', 'harga', 'link_gbr','tgl_input','id_jenis')
    list_filter = ('id_jenis__nama',)
    search_fields = ('nama','kdbrg','id_jenis__nama')
    list_per_page = 3

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
admin.site.register(About)