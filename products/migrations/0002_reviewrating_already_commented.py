# Generated by Django 3.2.25 on 2024-04-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='already_commented',
            field=models.BooleanField(default=False),
        ),
    ]
