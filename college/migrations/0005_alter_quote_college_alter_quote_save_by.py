# Generated by Django 5.0.1 on 2024-01-07 07:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("college", "0004_quote"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="college",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="college",
                to="college.college",
            ),
        ),
        migrations.AlterField(
            model_name="quote",
            name="save_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
