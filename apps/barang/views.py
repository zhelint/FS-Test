'''
    The views in here are ordered as below: 
    - CRUD for KategoriBarang, usually with the ending "kategori_barang"
    - CRUD for Barang, usually with the ending "barang"
    - CRUD for SatuanBarang, usually with the ending "satuan_barang"
'''

from wsgiref import headers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from apps.barang.forms import KategoriBarangForm, BarangForm, SatuanBarangCreateForm, SatuanBarangUpdateForm
from .models import KategoriBarang, Barang, SatuanBarang

def index(request):
    return render(request, 'barang/index.html')

def dashboard(request):
    return render(request, 'dashboard/index.html')
   
'''
    Views for KATEGORI BARANG
'''
def disp_kategori_barang(request):
    # display by created_at, but descending
    kategori_barang = KategoriBarang.objects.all().order_by('-created_at')

    template_name = 'barang/kategori/index.html'  
    if request.htmx:  
        template_name = 'barang/kategori/list-kategori-barang.html'  

    page_number = request.GET.get('page', 1)
    paginator = Paginator(kategori_barang, 20)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, template_name, context)

def add_kategori_barang(request):
    if request.method == 'POST':
        form = KategoriBarangForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'kategoriListReload'})
    else:
        form = KategoriBarangForm()
    context = {
        'form': form
    }
    return render(request, 'barang/kategori/add-form.html', context)

def update_kategori_barang(request, pk):
    kategori_barang = get_object_or_404(KategoriBarang, pk=pk)
    if request.method == 'POST':
        form = KategoriBarangForm(request.POST, instance=kategori_barang)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'kategoriListReload'})
    else:
        form = KategoriBarangForm(instance=kategori_barang)
    context = {
        'form': form
    }
    return render(request, 'barang/kategori/update-form.html', context)

def delete_kategori_barang(request, pk):
    kategori_barang = get_object_or_404(KategoriBarang, pk=pk)
    kategori_barang.delete()
    return HttpResponse(status=204, headers={'HX-Trigger': 'kategoriListReload'})


'''
    Views for BARANG
'''
def disp_barang(request):
    barang = Barang.objects.all().order_by('-created_at')

    template_name = 'barang/barang/index.html'
    if request.htmx:
        template_name = 'barang/barang/list-barang.html'

    page_number = request.GET.get('page', 1)
    paginator = Paginator(barang, 20)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }

    response = render(request, template_name, context)
    response['Vary'] = 'HX-Request'
    return response

def add_barang(request):
    if request.method == 'POST':
        form = BarangForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'barangListReload'})
    else:
        form = BarangForm()
    context = {
        'form': form
    }
    return render(request, 'barang/barang/add-form.html', context)

def update_barang(request, pk):
    barang = get_object_or_404(Barang, pk=pk)
    # print(f'barang: {barang.dict()}\n')

    if request.method == 'POST':
        # print(f'request.POST: {request.POST}\n')
        form = BarangForm(request.POST, instance=barang)
        # print(f'form: {form}\n')
        if form.is_valid():
            # print(f'form.cleaned_data: {form.cleaned_data}\n')
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'barangListReload'})
    else:
        form = BarangForm(instance=barang)

    barang_name = barang.nama_barang

    context = {
        'form': form,
        'barang_name': barang_name
    }
    return render(request, 'barang/barang/update-form.html', context)

def delete_barang(request, pk):
    barang = get_object_or_404(Barang, pk=pk)
    barang.delete()
    return HttpResponse(status=204, headers={'HX-Trigger': 'barangListReload'})

'''
    Views for SATUAN BARANG
'''
def disp_satuan_barang(request, barang_id):
    satuan_barang = SatuanBarang.objects.filter(kelompok=barang_id).order_by('-created_at')

    template_name = 'barang/satuan_barang/index.html'
    if request.htmx:
        template_name = 'barang/satuan_barang/list-satuan-barang.html'

    page_number = request.GET.get('page', 1)
    paginator = Paginator(satuan_barang, 20)
    page_obj = paginator.get_page(page_number)

    # check if satuan_barang is not empty
    if len(satuan_barang) > 0:
        nama_barang = satuan_barang.first().kelompok.nama_barang
    else:
        nama_barang = Barang.objects.get(pk=barang_id).nama_barang
    context = {
        'page_obj': page_obj,
        'barang_id': barang_id,
        'nama_barang': nama_barang
    }
    return render(request, template_name, context)


def add_satuan_barang(request, barang_id):
    if request.method == 'POST':
        # get the data inside the inputted form 
        form = SatuanBarangCreateForm(request.POST)
        if form.is_valid():
            qty = form.cleaned_data['qty']
            # create SatuanBarang object as much as qty
            for i in range(qty):
                satuan_barang = SatuanBarang(kelompok=Barang.objects.get(pk=barang_id))
                satuan_barang.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'satuanListReload'})
    else:
        form = SatuanBarangCreateForm()
    context = {
        'form': form
    }
    return render(request, 'barang/satuan_barang/add-form.html', context)

def update_satuan_barang(request, pk):
    satuan_barang = get_object_or_404(SatuanBarang, pk=pk)
    if request.method == 'POST':
        form = SatuanBarangUpdateForm(request.POST, instance=satuan_barang)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'satuanListReload'})
    else:
        form = SatuanBarangUpdateForm(instance=satuan_barang)

    kode_barang = satuan_barang.kode_barang
    kelompok = satuan_barang.kelompok.nama_barang

    context = {
        'form': form,
        'kode_barang': kode_barang,
        'kelompok': kelompok
    }
    return render(request, 'barang/satuan_barang/update-form.html', context)

def delete_satuan_barang(request, pk):
    satuan_barang = get_object_or_404(SatuanBarang, pk=pk)
    satuan_barang.delete()
    return HttpResponse(status=204, headers={'HX-Trigger': 'satuanListReload'})