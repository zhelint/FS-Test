from django import forms
from .models import KategoriBarang, Barang, SatuanBarang
# from django.contrib.admin.widgets import AutocompleteSelect
# from django.contrib import admin

class KategoriBarangForm(forms.ModelForm):
    class Meta:
        model = KategoriBarang
        fields = ['nama']

class BarangForm(forms.ModelForm):
    # kategori = forms.ModelChoiceField(
    #     queryset=KategoriBarang.objects.all(),
    #     widget=AutocompleteSelect(
    #         Barang._meta.get_field('kategori').remote_field,
    #         admin.site,
    #     )
    # )

    class Meta:
        model = Barang
        fields = ['nama_barang', 'merk', 'kategori', 'stok']

class SatuanBarangCreateForm(forms.Form):
    qty = forms.IntegerField(label='Qty Barang', min_value=1)

class SatuanBarangUpdateForm(forms.ModelForm):
    class Meta:
        model = SatuanBarang
        fields = ['kondisi']