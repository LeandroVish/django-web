# Generated by Django 5.0.2 on 2024-10-18 11:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_itenscompra"),
    ]

    operations = [
        migrations.AddField(
            model_name="compra",
            name="data",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="itenscompra",
            name="preco",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
