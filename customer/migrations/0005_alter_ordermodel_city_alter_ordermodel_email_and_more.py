# Generated by Django 5.1.3 on 2024-11-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='state',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='street',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
