# Generated by Django 4.2.6 on 2023-11-06 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.TextField(max_length=8, verbose_name='rol'),
        ),
    ]
