# Generated by Django 5.0.6 on 2024-05-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0005_alter_kelompokbarang_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satuanbarang',
            name='kode_barang',
            field=models.CharField(default=None, editable=False, max_length=50, null=True, unique=True),
        ),
    ]