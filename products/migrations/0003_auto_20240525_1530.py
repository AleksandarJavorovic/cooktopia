# Generated by Django 3.2.25 on 2024-05-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_reviewrating_already_commented"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="country_of_origin",
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="diametar",
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="material",
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="volume",
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
