# Generated by Django 3.2.6 on 2024-05-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelompokbarang',
            name='prefix',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
