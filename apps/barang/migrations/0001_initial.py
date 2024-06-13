# Generated by Django 3.2.6 on 2024-05-25 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriBarang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='KelompokBarang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=50)),
                ('merk', models.CharField(max_length=50)),
                ('stok', models.IntegerField(default=0)),
                ('prefix', models.CharField(editable=False, max_length=8, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barang.kategoribarang')),
            ],
        ),
        migrations.CreateModel(
            name='SatuanBarang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_barang', models.CharField(editable=False, max_length=50, unique=True)),
                ('kondisi', models.CharField(choices=[('bagus', 'Bagus'), ('rusak', 'Rusak'), ('perlu_perbaikan', 'Perlu Perbaikan'), ('dlm_perbaikan', 'Dalam Perbaikan')], default='bagus', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kelompok', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barang.kelompokbarang')),
            ],
        ),
    ]