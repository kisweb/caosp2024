# Generated by Django 5.0.1 on 2024-01-06 09:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ief", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ief",
            old_name="created_by",
            new_name="responsable",
        ),
    ]
