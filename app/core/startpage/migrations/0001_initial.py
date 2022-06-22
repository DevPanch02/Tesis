# Generated by Django 4.0 on 2022-06-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio_tit', models.IntegerField(blank=True, default=0, null=True)),
                ('num_reg', models.IntegerField(blank=True, default=0, null=True)),
                ('RUC', models.CharField(blank=True, default='', max_length=13, null=True)),
                ('nombrecomercial', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('razonsocial', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('calleprincipal', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('numerocasa', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('callesecundaria', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('sector', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('patrimonio', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('ced_ruc_representante', models.CharField(blank=True, default='', max_length=13, null=True)),
                ('nombrerepresentante', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('apellidorepresentante', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('negociotipo', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('describenegocio', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('rubro_pagado', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('valorpagar', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('fechpago', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('estadotitulo', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('fecharuc', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('fecharegmunicipio', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('abiertocerrado', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('fechacierre', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('canton_ruc', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('provincia_ruc', models.CharField(default=False, max_length=50)),
                ('peticiones', models.IntegerField(default=0)),
                ('descripcion', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
    ]