# Generated by Django 5.0.1 on 2024-01-12 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnneeScolaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(db_index=True, max_length=9, unique=True)),
                ('statut', models.CharField(blank=True, default='AnneeEnCours', max_length=20)),
            ],
            options={
                'verbose_name': 'AnneeScolaire',
                'verbose_name_plural': 'AnneeScolaires',
            },
        ),
    ]
