# Generated by Django 3.2.8 on 2021-10-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0004_orderla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='hdd',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='screensize',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ssd',
            field=models.CharField(max_length=20),
        ),
    ]
