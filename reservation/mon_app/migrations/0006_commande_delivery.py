# Generated by Django 5.0.6 on 2024-05-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0005_commande_email_commande_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='delivery',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
