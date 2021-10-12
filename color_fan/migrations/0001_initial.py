# Generated by Django 3.2.6 on 2021-10-04 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='colorfan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('original_price', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('primary_camera', models.IntegerField()),
                ('secondary_camera', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('coverphoto', models.ImageField(upload_to='')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='user_enquiry1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('full_name', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField()),
                ('district', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='', max_length=20)),
                ('priceo', models.IntegerField()),
                ('coverphotoo', models.ImageField(upload_to='')),
                ('dateorder', models.DateTimeField(default=None, null=True)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
