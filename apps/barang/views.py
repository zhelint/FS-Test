from django.shortcuts import render


# Create your views here.
def barang(request):
    return render(request, 'barang/index.html')
