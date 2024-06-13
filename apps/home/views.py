from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from apps.barang.models import SatuanBarang, Barang


# Create your views here.

def dashboard(request):

    '''
        GPT said it's more efficient to use a single query to get all the data
        and then organize it in Python data, rather than making multiple queries.
        I'm not sure if this is the best way to do it, but it works.
    '''

    # Get the SatuanBarang data grouped by kelompok and kondisi
    # and count the number of items in each group

    # This query is equivalent to the following SQL query:
    # SELECT kelompok.nama_barang AS kelompok__nama_barang, kondisi, COUNT(id) AS total
    # FROM barang_satuanbarang
    # GROUP BY kelompok.nama_barang, kondisi;

    barang_by_kondisi = SatuanBarang.objects.\
        values('kelompok__nama_barang', 'kondisi').\
        annotate(total=Count('id')).\
        order_by('kelompok__nama_barang')
    
    # Organize data into separate lists for each condition
    data_by_kondisi = {
        'bagus': [],
        'rusak': [],
        'perlu_perbaikan': [],
        'dlm_perbaikan': []
    }

    counts = {
        'bagus': 0,
        'rusak': 0,
        'perlu_perbaikan': 0,
        'dlm_perbaikan': 0
    }
    
    # Insert each data into the right kondisi list
    for item in barang_by_kondisi:
        kondisi = item['kondisi']
        data_by_kondisi[kondisi].append(item)
        counts[kondisi] += item['total']
        
    context = {
        'brg_bagus': data_by_kondisi['bagus'],
        'brg_rusak': data_by_kondisi['rusak'],
        'brg_perlu_perbaikan': data_by_kondisi['perlu_perbaikan'],
        'brg_dlm_perbaikan': data_by_kondisi['dlm_perbaikan'],
        'bagus_count': counts['bagus'],
        'rusak_count': counts['rusak'],
        'perlu_perbaikan_count': counts['perlu_perbaikan'],
        'dlm_perbaikan_count': counts['dlm_perbaikan']
    }

    return render(request, 'dashboard/index.html', context)
