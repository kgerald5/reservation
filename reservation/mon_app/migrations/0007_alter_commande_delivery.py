# Generated by Django 5.0.6 on 2024-05-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0006_commande_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='delivery',
            field=models.DateField(),
        ),
    ]
