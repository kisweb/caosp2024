# Generated by Django 5.0.1 on 2024-01-11 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_college_slug_alter_quote_annee_scolaire_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='quote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quote', to='college.quote'),
        ),
        migrations.AlterField(
            model_name='college',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_by', to=settings.AUTH_USER_MODEL),
        ),
    ]