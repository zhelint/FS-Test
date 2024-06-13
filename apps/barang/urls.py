
from django.urls import path
from . import views
from django.conf import settings

'''
    The URLs are ordered in the following sequence:
    1. Kategori Barang --> Disp, Add, Update, Delete
    2. Barang --> Disp, Add, Update, Delete
    3. Satuan Barang --> Disp, Add, Update, Delete
'''

urlpatterns = [

    # Kategori Barang page
    path('kategori', views.disp_kategori_barang, name='disp_kategori_barang'),
    path('add-kategori', views.add_kategori_barang, name='add_kategori_barang'),
    path('update-kategori-barang/<int:pk>', views.update_kategori_barang, name='update_kategori_barang'),
    path('delete-kategori-barang/<int:pk>', views.delete_kategori_barang, name='delete_kategori_barang'),


    # Barang page 
    path('barang', views.disp_barang, name='disp_barang'),
    path('add-barang', views.add_barang, name='add_barang'),
    path('update-barang/<int:pk>', views.update_barang, name='update_barang'),
    path('delete-barang/<int:pk>', views.delete_barang, name='delete_barang'),


    # Satuan Barang page
    path('detail-barang/<int:barang_id>', views.disp_satuan_barang, name='disp_satuan_barang'),
    path('add-satuan-barang/<int:barang_id>', views.add_satuan_barang, name='add_satuan_barang'),
    path('update-satuan/<int:pk>', views.update_satuan_barang, name='update_satuan_barang'),
    path('delete-satuan/<int:pk>', views.delete_satuan_barang, name='delete_satuan_barang'),
    
]