from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class KategoriBarang(models.Model):
    nama = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
    

class Barang(models.Model):
    nama_barang = models.CharField(max_length=50, blank=False)
    merk = models.CharField(max_length=50, blank=False)
    kategori = models.ForeignKey(KategoriBarang, on_delete=models.SET_NULL, null=True)
    stok = models.IntegerField(default=0, blank=False)
    # Does this make sense? 
    prefix = models.CharField(max_length=8, unique=True, editable=False, blank=False, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_barang


class SatuanBarang(models.Model):
    kode_barang = models.CharField(max_length=50, blank=False, unique=True, editable=False, null=True, default=None)
    kondisi_choices = (
        ('bagus', 'Bagus'),
        ('rusak', 'Rusak'),
        ('perlu_perbaikan', 'Perlu Perbaikan'),
        ('dlm_perbaikan', 'Dalam Perbaikan'),
    )
    kondisi = models.CharField(max_length=50, choices=kondisi_choices, default='bagus')
    kelompok = models.ForeignKey(Barang, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kode_barang
    
@receiver (post_save, sender=Barang)
def create_prefix(sender, instance, created, **kwargs):
    if created:
        if(len(instance.merk) > 3):
            instance.prefix = f"{instance.merk[:4].upper()}{str(instance.id).zfill(4)}"
        else:
            instance.prefix = f"{instance.merk.upper()}{str(instance.id).zfill(4)}"
        instance.save()

        # Create SatuanBarang instances based on stok
        for i in range(instance.stok):
            SatuanBarang.objects.create(
                kode_barang=None,  # Placeholder, will be set by the SatuanBarang post_save signal
                kelompok=instance
            )

@receiver (post_save, sender=SatuanBarang)
def create_kode_barang(sender, instance, created, **kwargs):
    if created:
        instance.kode_barang = f"{instance.kelompok.prefix}-{str(instance.id).zfill(4)}"
        instance.save()
