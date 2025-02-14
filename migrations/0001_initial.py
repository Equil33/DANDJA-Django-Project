# Generated by Django 5.1.3 on 2025-02-13 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite_stock', models.PositiveIntegerField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('date_vente', models.DateTimeField(auto_now_add=True)),
                ('mode_paye', models.CharField(max_length=20)),
                ('prix_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.produit')),
            ],
        ),
    ]
