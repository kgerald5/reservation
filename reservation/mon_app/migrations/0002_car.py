# Generated by Django 5.0.6 on 2024-05-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('color', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
