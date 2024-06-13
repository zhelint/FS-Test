from django.contrib import admin
from .models import KategoriBarang, Barang, SatuanBarang

# Register your models here.
admin.site.register(KategoriBarang)
admin.site.register(Barang)
admin.site.register(SatuanBarang)