# Generated by Django 5.0.6 on 2024-05-25 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0002_alter_kelompokbarang_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelompokbarang',
            name='prefix',
            field=models.CharField(editable=False, max_length=8, unique=True),
        ),
    ]
